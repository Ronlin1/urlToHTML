from urlToHTML import urltohtml 

initiate = urltohtml.Blog()
save_blog = initiate.save("https://blog.octachart.com/", "test_file")

print(save_blog)

# You can create multiple URLs to loop from and saving them to 
# a different name every loop;

