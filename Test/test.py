from urlToHTML import urltohtml 

initiate = urltohtml.Blog()
save_blog = initiate.save("https://blog.octachart.com/", "test_file")
print(save_blog)