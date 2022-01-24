class WordDictionary:

    def __init__(self):
        self._word_dic = {'end': False}

    def addWord(self, word: str) -> None:
        dic = self._word_dic
        for i in range(len(word)):
            if word[i] not in dic:
                end = False
                if i == len(word) - 1:
                    end = True
                dic[word[i]] = {'end': end}
            elif i == len(word) - 1:
                dic[word[i]]['end'] = True
            dic = dic[word[i]]

    def search(self, word: str) -> bool:
        dics = [self._word_dic, ]
        for i in range(len(word)):
            # if word[i] == '.':
            tmp_dics = []
            for dic in dics:
                if word[i] == '.':
                    for any_key, any_value in dic.items():
                        if any_key != 'end':
                            if i == len(word) - 1:
                                if any_value['end'] == True:
                                    return True
                            else:
                                tmp_dics.append(any_value)
                elif word[i] in dic:
                    tmp_dics.append(dic[word[i]])
                    if i == len(word) - 1 and dic[word[i]]['end']:
                        return True
            dics = tmp_dics
        return False


# Your WordDictionary object will be instantiated and called as such:
if __name__ == '__main__':
    obj = WordDictionary()
    obj.addWord('ad')
    param_2 = obj.search('a.')
    print(param_2)
