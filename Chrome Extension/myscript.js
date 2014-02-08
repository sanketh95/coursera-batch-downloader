var jsondata='';
var coursename = location.pathname.match(/\/(.*)\//)[1];

$('.course-item-list-header').each( function(index, val){
	var name = $('h3',this).html();
	var selection_list = $('.course-item-list-section-list:eq('+index+')');
	var pattern = new RegExp('nbsp;[ \t]*(.*)');
	var re = pattern.exec(name);
	var fname = re[re.length-1	];

	jsondata = jsondata+'{ "title" : "'+fname+'","links":[';
	$('li',selection_list).each(function(ind, val){
		var linkaddr = $('a:last-child',$('.course-lecture-item-resource',this)).attr('href');
		var title=$('a', this).html();
		title = title.replace(/^\s+|\s+$/g,'')	
		jsondata = jsondata+'{"title":"'+title+'","link":"'+linkaddr+'"},';
	});
	jsondata= jsondata.replace(/(^,)|(,$)/g , '');
	jsondata+=']},'

});

jsondata= jsondata.replace(/(^,)|(,$)/g , '');
console.log('{"cname":"'+coursename+'","data":['+jsondata+']}');