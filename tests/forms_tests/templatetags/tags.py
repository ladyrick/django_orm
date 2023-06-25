from django_orm.template import Library, Node

register = Library()


class CountRenderNode(Node):
    count = 0

    def render(self, context):
        self.count += 1
        for v in context.flatten().values():
            try:
                v.render()
            except AttributeError:
                pass
        return str(self.count)


@register.tag
def count_render(parser, token):
    return CountRenderNode()
