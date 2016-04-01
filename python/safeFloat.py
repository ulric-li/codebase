#!/usr/bin/env python3

'''
计算carddata.txt中纯数字行的和
非纯数字的行，输出的日志中
'''

def safe_float(obj):
    ''' safe version of float()'''
    try:
        retval = float(obj)
    except (ValueError, TypeError) as e:
        retval = str(e)
    return retval

def main():
    ''' handles all the data processing'''
    log = open('cardlog.txt', 'w')
    try:
        ccfile = open('carddata.txt', 'r')
        txns = ccfile.readlines()
        ccfile.close()
    except IOError as e:
        log.write('no txns this month\n')
        log.close()
        return

    total = 0.00
    log.write('account log:\n')

    for eachTxn in txns:
        result = safe_float(eachTxn)
        if isinstance(result, float):
            total += result
            log.write('data(%f).. processed\n' % result)
        else:
            log.write('ignored:%s' % result)

    print ('%.2f (new balance)' % total)
    log.close()


if __name__ == '__main__':
    main()
