import requests_html


def my_download(word='李小龙', pn=1):
    sess = requests_html.HTMLSession()
    baidu_url = 'http://image.baidu.com/search/index?tn=baiduimage&ie=utf-8&word='
    pn_per_page = 30
    reg = '"thumbURL":"{}"'
    addr_list = [j[0] for i in range(pn) for j in sess.get(f'{baidu_url}{word}&pn={pn_per_page*i}').html.search_all(reg)]
    return addr_list


def my_save_img(my_dir, addr_list, file_name='李小龙'):
    import os
    if not os.path.exists(my_dir):
        os.makedirs(my_dir)
    sess = requests_html.HTMLSession()
    for num, addr1 in enumerate(addr_list,1):
        try:
            resp = sess.get(addr1)  # write to file
            with open(f'{my_dir}/{file_name}_{num}.jpg', 'wb') as f:
                f.write(resp.content)
        except:
            pass  # empty, make sure the format is right


# word = '李小龙'
# img_list = my_download(word)
# my_save_img(f'download/{word}', img_list, word)
