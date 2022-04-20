from django import template

register = template.Library()


#リクエストオブジェクトのキーを指定し値を書き換える。
@register.simple_tag()
def url_replace(request, key, value):
    #ここでリクエストのボディをコピー(辞書型で複製する)
    copied          = request.GET.copy()

    #{"order_by":"","search":"商品","page":"1"}

    #keyの値をvalueに書き換える(keyが"page"、valueが"2"の場合)
    copied[key]     = value

    #{"order_by":"","search":"商品","page":"2"}

    return copied.urlencode()
    
    # order_by=&search=商品&page=2





