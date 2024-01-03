"""
    Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file system,
    convert it to the simplified canonical path.

    In a Unix-style file system, a period '.' refers to the current directory, a double period '..' refers to the directory up a level, 
    and any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'. 

    For this problem, any other format of periods such as '...' are treated as file/directory names.
"""

class Solution:
    def simplifyPath(self, path) -> str:
        can_path = "/"
        if len(path) < 2:
            return can_path
        stack = []
        period_cnt = 0
        p = 0
        prev = None
        dir_cnt = 0
        letter_cnt = 0
        while p < len(path):
            if path[p] == '.':
                period_cnt += 1
                stack.append('.')
            elif path[p] == '/':
                if period_cnt > 0 and period_cnt <= 2 and letter_cnt < 1:
                    dir_cnt = period_cnt
                    if stack:
                        while stack and dir_cnt > 0:
                            if stack[-1] == '/':
                                dir_cnt -= 1
                            stack.pop()
                    period_cnt = 0
                    stack.append((path[p]))
                elif prev and prev != '/' and p < len(path) - 1:
                    stack.append('/')
                letter_cnt = 0
            else:
                period_cnt = 0
                letter_cnt += 1
                stack.append(path[p])
            prev = path[p]
            p += 1
        if period_cnt > 0 and period_cnt <= 2 and letter_cnt < 1:
            dir_cnt = period_cnt
            if stack:
                while stack and dir_cnt > 0:
                    if stack[-1] == '/':
                        dir_cnt -= 1
                    stack.pop()
            period_cnt = 0
    
        if stack:
            i = len(stack)
            size = len(stack)
            while i >= size:
                if stack[i - 1] == '/':
                    stack.pop()
                    i -= 1
                else:
                    break
            if  stack and stack[0] == '/':
                del [stack[0]]
            for i in stack:
                can_path += i
        return can_path
    """ The above has a time complexity of O(n) and space complexity of O(n)"""
    def simplifyPath2(self, path) -> str:
        result = []
        for part in path.split('/'):
            if part == '..':
                if len(result):
                    result.pop()
            elif len(part) and part != '.':
                result.append(part)
        return '/' + '/'.join(result)
    """ Time complexity is O(3n) and space is O(2n)"""
if __name__ == '__main__':
    instance = Solution()
    path1 = "/a/./b/../../c/"
    path2 = "/home//foo/"
    path3 = "/a//b////c/d//././/.."

    print(instance.simplifyPath2(path1))
