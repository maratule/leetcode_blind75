from typing import List
l = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
def reorderLogFiles(self, logs: List[str]) -> List[str]:
    let = []
    dig = []
    for log in logs:
        log_content = log.split(' ', 1)[1]
        if (ord(log_content[0]) >= ord('0') and ord(log_content[0]) <= ord('9')):
            dig.append(log)
        else:
            let.append(log)
    print(dig)
    print(let)
    return
reorderLogFiles(logs=l)

