

def replace_all_space(url):

    url_list = list(url)
    for i in range(len(url_list)):
        if url_list[i] == " ":
            url_list[i] = "%20"
    return "".join(url_list)




def replace_all_space(url):
    return url.replace(" ", "%20")

replaced = replace_all_space("jf fdf ")

print(replaced)