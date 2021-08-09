import graphene
import json
from datetime import datetime

class User(graphene.ObjectType):
    id = graphene.ID()
    username = graphene.String()
    last_login = graphene.DateTime(required=False)

class Query(grapheve.ObjectType):
    users = graphene.List(User, first=graphene.Int())

    def resolve_users(self, info, first):
        return [
            User(userName='Alice', last_login=datetime.now()),
            User(userName='Bob', last_login=datetime.now()),
            User(userName='steve', last_login=datetime.now()),
        ][:first]

class CreateUser(graphene.Mutation):

    class Arguments:
        username = graphene.string()

    user = graphene.Field(User)

    def mutate(self, info, username)
        if info.context.get('is_vip'):
            username = username.upper()

        user = User(username=username)
        return CreateUser(user=user)

class Mutations(graphene.ObjectType):
        create_user = CreateUser.Field()

schema = graphene.Schema(query=Query, mutation=Mutations)


restult = schema.execute(
        '''
        mutation createUser($useranme: String) {
            createUser(username: "$username") {
                user {
                    username
                }
            }
        }
        ''',
        variable_values={'username': 'Alice'},
        context={'is_vip': False}
    )



items = dict(result.data.items())
print(json.dumps(items, indent=4))
