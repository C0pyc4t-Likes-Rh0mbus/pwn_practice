1. File Descriptor 란?
리눅스에서는 파일이 오픈되고 나면 file descriptor라는 일종의 Index 번호가 반환됨.
FD 는 파일을 오픈한 프로세스의 고유 번호이다. 

프로세스마다 관례적으로 0,1,2 은 사전 배정되어 있는데 
0 : 표준 입력(stdin)
1 : 표준 출력(stdout) 
2 : 표준 오류(stderr)

* reference : http://noplanlife.com/?p=1211

2. 문제 풀이 
![fd_source_img](../img/fd_source_img.png)


