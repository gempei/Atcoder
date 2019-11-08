import sys
def thinking(all_cl,users_cl,failnum):
    others_cl = users_cl
    others_cl.pop(failnum)
    print(others_cl)
    condcl = list(set(all_cl) - set(others_cl))
    print(condcl)
    del_cl = []
    for card in condcl:
        for i in range(failnum):
            sim_users_cl = others_cl.copy()
            sim_users_cl.insert(failnum,card)
            if(thinking(all_cl,sim_users_cl,i) != "?"):
                del_cl.append(card)
                print("del")
                print(del_cl)
    condcl = list(set(condcl) - set(del_cl))

    maxnum = max(condcl)
    minnum = min(condcl)


    cond_ansl = []
    if(maxnum < min(others_cl)):
        cond_ansl.append("MIN")
    if(minnum > max(others_cl)):
        cond_ansl.append("MAX")
    if(maxnum < max(others_cl) and minnum > min(others_cl)):
        cond_ansl.append("MID")

    if(len(cond_ansl) == 1):
        return cond_ansl[0]
    else:
        return "?"

def main():
    if(len(sys.argv)!=4):
        print("invalid status")

    users_cldic = {}
    N = 5
    all_cl = [i for i in range(1,N+1)]
    for user_info in sys.argv[1:]:
        name,number_str = user_info.split("=")
        users_cldic[name] = int(number_str)

    ans_l = []
    for failnum in range(len(users_cldic)):
        ans_l.append(thinking(all_cl,list(users_cldic.values()),failnum))
        print(ans_l)
        if(ans_l[failnum] is not  "?"):
            break

    print(ans_l)


if __name__ == '__main__':
    main()
