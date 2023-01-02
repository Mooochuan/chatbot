import my_chat_function as cf
import my_baidu_img_dwn as bd_dwn

# Doing conversation
chat_list = ['Hi', 'Hello, how can I help you?', 'What is the weather like?', 'Rainy today', 'Goodbye']
cmd_list = ['Tell me the time', 'Draw a Peppa Pig', 'Open Google', 'Download or Search']
i = 0

'''
# A new question
1. check cur_rate 0
2. no such question
    Solution：
        Explain to the user the question is not in the storage and ask how to answer
        add the answer in chat_list
# Save conversation content
1. Read the file first
2. Append to the file when no answer
'''
# chat_list upgrade
try:
    with open('mychat.txt', 'r', encoding='utf8') as f:
        chat_list = f.read().split('\n')
    # Every string has newline character in the end except the last one
except FileNotFoundError:
    # FileNotFoundError: [Errno 2] No such file or directory: 'mychat.txt'
    print('No conversation content!')


print('Peppa: ', 'Hello!')
while True:
    a = input('Michael: ')
    # Exit command
    if a == 'Exit':
        break
    # Compare a with strings in chat_list and choose the most similar one
    # print('Peppa:', chat_list[chat_list.index(a) + 1])
    cur_index_chat, cur_rate_chat = cf.get_chat_str_index(a, chat_list)
    cur_index_cmd, cur_rate_cmd = cf.get_chat_str_index(a, cmd_list)
    # Check which one is the most similar and cmd chat
    if cur_rate_cmd > cur_rate_chat:
        cur_rate = cur_rate_cmd
        cur_index = cur_index_cmd
        if cmd_list[cur_index] == 'Tell me the time':
            import clock
            clock.draw_time()
            print('Peppa: ', 'I have drawn you a clock')
        elif cmd_list[cur_index] == 'Draw a Peppa Pig':
            import peiqi
            peiqi.my_draw_peiqi()
            print('Peppa: ', 'I have drawn you a Peppa')
        elif cmd_list[cur_index] == 'Open Google':
            import webbrowser
            webbrowser.open('www.google.com')
            print('Peppa: ', 'I have opened Google')
        elif cmd_list[cur_index] == 'Download or Search':
            # Download"word"
            word = a[a.index('“')+1:a.index('”')]
            page_num = 2
            img_list = bd_dwn.my_download(word, page_num)
            bd_dwn.my_save_img(f'download/{word}', img_list, word)
            print('Peppa: ', f'I have downloaded{word}，and saved to download/{word} path.')
    else:
        cur_rate = cur_rate_chat
        cur_index = cur_index_chat
        if cur_rate < 1:
            print('Peppa: ', 'I do not have this question in my storge. Could you please teach me?1: Yes, 2: No')
            b = input('Michael: ')
            if b == '1':
                print('Peppa: ', 'I am ready to receive, please type')
                c = input('Michael: ')
                # append
                chat_list.append(a)
                chat_list.append(c)
                print('Michael: ', 'I have received, thanks')
                # save after append
                with open('mychat.txt', 'w', encoding='utf8') as f:
                    f.write('\n'.join(chat_list))
                    # f.writelines(chat_list)
            else:
                cur_index = -1
        print('Peppa: ', chat_list[(cur_index + 1) % chat_list.__len__()])
