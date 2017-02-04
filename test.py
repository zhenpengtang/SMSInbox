
def getSMSList():
    sms_list=[]
    f=open("sms\data.txt","r")
    sms_list=f.readlines()
    f.close()
    return sms_list



def get_sms_list_sort(sms_list):
    sms_list_sort=[]
    k=len(sms_list)
    print k
    for i in range(k):
        sms_list_sort.append(sms_list[(k-1-i)])
        #print sms_list[k-1-i]
    return sms_list_sort

sms_list=getSMSList()
get_sms_list_sort(sms_list)