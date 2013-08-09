<h1>Installation instructions<h1>
<h1>This project is experimental<h1>	
<h3>Dependencias</h3>
<ul>
	<li>django-mppt</li>
	<li>python-twitter</li>
	<li>python-facebook</li>
	<li>python pil</li>
</ul>

<h3>urls for blog</h3>

		{% url apps.blog.views.article_details year=notice.getYear month=notice.getMonth day=notice.getDay slug=notice.slug %}"> VEr noticia
  			
       {% url apps.blog.views.article_details_slug id=notice.id slug=notice.slug %}"> VEr noticia 2

  		"/{{Slug}}/{{notice.id}}-{{notice.slug}}" VEr noticia 3
        
       {% url apps.blog.views.article_details_slug_category id=notice.id category_slug=Category.slug slug=notice.slug  %} VEr noticia 4
        
        {% url apps.blog.views.article_details_slug_category_date year=notice.getYear month=notice.getMonth day=notice.getDay id=notice.id category_slug=Category.slug slug=notice.slug %} VEr noticia 5