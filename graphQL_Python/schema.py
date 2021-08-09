import graphene

class Query(grapheve.ObjectType):
    is_staff = graphene.Boolean()

    def resolve_is_staff(self, info):
        return True

    schema = graphene.Schema(query=Query)

    restult = schema.execute(
        '''
        {
            isStaff
        }
        '''
    )

items = dictionary(result.data.items())
print(json.dumps(items, indent=4))
