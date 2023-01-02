import numpy as np
import os

from flask import Flask, render_template, request, jsonify

my_app = Flask(__name__)

icon_tag_list = {'robot': {'img': '/static/img/dhf.jpg', 'imgcss': 'imgleft', 'spancss': 'spanleft'},
                 'user': {'img': '/static/img/z.jpg', 'imgcss': 'imgright', 'spancss': 'spanright'}}

user_chat_content = {
    'username': 'Master',
    'icontag': [('robot', 'Hello Master, how may I help you?'), ]
}


@my_app.route('/')
def my_welcome():
    return render_template('chat2.html', chat_content=user_chat_content, icon_tag=icon_tag_list)


# chat UI
@my_app.route('/chatres', methods=['POST', 'GET'])
def my_chat():
    con = request.form['con']  # get parameter, or request.args.get()
    user_chat_content['icontag'].append(('user', con))
    # add content
    user_chat_content['icontag'].append(('robot', my_chat_response.chat_response(con)))

    return render_template('chat2.html', chat_content=user_chat_content, icon_tag=icon_tag_list)


# img download and present UI
@my_app.route('/download/<content>')
def my_show_img(content):
    # check the img
    img_list = [f'{content}/{i}' for i in os.listdir(f'static/download/{content}') if os.path.splitext(i)[1] == '.jpg']
    return render_template('imgshow.html', img_list=img_list)


# img wall process
@my_app.route('/repage/<img_name>', methods=['GET'])
def my_repage_show(img_name):
    imgpath_ori = request.args.get('imgpath')
    if r'\u' in imgpath_ori:
        imgpath = request.args.get('imgpath').encode('unicode_escape').decode()
    elif r'\x' in imgpath_ori:
        imgpath = request.args.get('imgpath').encode('raw_unicode_escape').decode()
    else:
        imgpath = imgpath_ori
    # Process, Picture address list, list size is 100*100, one dimensional
    # imgpath format: ‘李小龙/李小龙_1.jpg’
    p_path_list = my_img_process.p_pic_wall_main(imgpath)
    return render_template('facepage.html', path_list=p_path_list)


@my_app.route('/test', methods=['GET'])
def my_repage_show_test():
    # test
    p_path_list = ['/static/download/李小龙_rect/rect_李小龙_1.jpg' for i in range(102)]
    return render_template('facepage.html', path_list=p_path_list)


@my_app.route('/api/mnist', methods=['POST'])
def mnist():
    input = ((255 - np.array(request.json, dtype=np.uint8)) / 255.0).reshape(1, 784)
    # Returns two lists, representing the corresponding recognition probabilities, regression  convolution
    output1 = [0.003, 0.01, 0.007, 0.89, 0.012, 0.008, 0.014, 0.007, 0.026, 0.023]
    output2 = [0.002, 0.007, 0.002, 0.932, 0.002, 0.008, 0.012, 0.006, 0.016, 0.013]

    return jsonify(results=[output1, output2])


@my_app.route('/mnist', methods=['GET'])
def mnist_main():
    return render_template('digital.html')


if __name__ == "__main__":
    my_app.run(debug=True)
