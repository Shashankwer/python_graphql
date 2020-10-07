import graphene
from graphene_django import DjangoObjectType
from django.utils import timezone
from .models import links  as Link, Vote
from users.schema import UserType
from graphql import GraphQLError
from django.db.models import Q

class LinkType(DjangoObjectType):
    class Meta:
        model =  Link

class VoteType(DjangoObjectType):
    class Meta:
        model=Vote

class Query(graphene.ObjectType):
    links = graphene.List(LinkType,
                        search=graphene.String(),
                        first=graphene.Int(),
                        skip=graphene.Int())
    votes = graphene.List(VoteType)
    def resolve_links(self,info,search=None,first=None,skip=None,**args):
        qs = Link.objects.all()
        if search:
            filter=(Q(url__icontains=search)|Q(description__icontains=search))
            qs = qs.filter(filter)
        if skip:
            qs = qs[skip:]
        if first:
            qs = qs[:first]
        return qs

    def resolve_votes(self,info,**kwargs):
        return Vote.objects.all()    

class CreateLink(graphene.Mutation):
    """
    Defines the mutation class
    Right after you define the mutation one can define the 
    data one can send back to the client. 
    The output is defiend field by field 
    So one can define only one field 
    """
    id = graphene.Int()
    url = graphene.String()
    description = graphene.String()
    updateDate = graphene.DateTime()
    postedBy = graphene.Field(UserType)

    class Arguments:
        #Data that can be sent to the server by client
        url = graphene.String()
        description = graphene.String()

    def mutate(self,info,url,description):
        #Mutation method
        user = info.context.user or None
        link = Link(url=url, description=description,posted_by=user)
        link.save()
        return CreateLink(
            id = link.id,
            url = link.url,
            description=link.description,
            updateDate = link.update_date,
            postedBy=link.posted_by
        )

class CreateVote(graphene.Mutation):
    user= graphene.Field(UserType)
    link = graphene.Field(LinkType)
    class Arguments:
        link_id = graphene.Int()
    
    def mutate(self,info,link_id):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError('User must be logged in')
        
        link = Link.objects.filter(id=link_id).first()
        if not link:
            raise Exception('Invalid Link!!')

        Vote.objects.create(
            user=user,
            link=link
        )

        return CreateVote(user=user,link=link)
    

class Mutation(graphene.ObjectType):
    #Mutation class that needs to be resolved. 
    create_link = CreateLink.Field()
    create_vote = CreateVote.Field()

