import os


def to_dict(path):
    file = open(path, "r", encoding='UTF8')
    list = file.read().split('\n')

    dic = {}
    for line in list:
        if not line:
            continue
        key, value = line.split(',')
        dic[key] = float(value)

    return dic


def txts_to_combine_dict(path, output):
    alpha = 0.8
    dic = {}

    file_dir = os.listdir(path)
    for i in range(len(file_dir)):
        factors = to_dict(path+file_dir[i])
        factors_items = factors.items()
        for key,value in factors_items:
            if key in dic:
                print(key + '라는 단어가 겹침!')
                dic[key] = alpha * dic[key] + (1 - alpha) * float(value)
            else:
                dic[key] = float(value)

    file = open(path + "/" + output, "w", encoding='UTF8')

    dic_items = dic.items()
    for key, value in dic_items:
        file.write('%s,%.4f\n' % (key, value))

    file.close()

    return dic
