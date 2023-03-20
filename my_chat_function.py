# Compare the input string with each one in chat_list and return the index
def get_chat_str_index(str1, chat_list):
    # rate_list = []  # save the result of comparing
    # for item in chat_list:
    #     rate_list.append(str_cmp_base_cnt(str1,item)[0])  # save the first one
    rate_list = [str_cmp_base_cnt(str1, item)[0] for item in chat_list]
    # find the index
    index_out = rate_list.index(max(rate_list))
    # index_out = [str_cmp_base_cnt(str1,item)[0] for item in chat_list].index(max(rate_list))
    return index_out, max(rate_list)


def str_cmp_base_cnt(str1, str2):
    # determine the cur_rate by counting same words
    cnt_word = 0
    str1_wordlist = str1.split( );
    str2_wordlist = str2.split( );
    for i in str1_wordlist:
        if i in str2_wordlist:
            cnt_word += 1
    cmp_rate = cnt_word * min(str1_wordlist.__len__() / str2_wordlist.__len__(), str2_wordlist.__len__() / str1_wordlist.__len__())
    return cmp_rate, cnt_word
