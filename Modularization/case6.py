def histogram(lst):
    histogram = '*'
    hist_lst = []
    for i in lst:
        for j in histogram:
            count = 0
            while count <= i:
                hist_lst.append('*')
                count = count + 1
                if count == i:
                    print('')
                    for k in hist_lst:
                        print(k, end='') #I'm not sure why this affects the way the program prints the multiline k tbh
                        hist_lst = []
                    break

histogram([4,6,10])
histogram([1,2,3])
histogram([5,7,1])