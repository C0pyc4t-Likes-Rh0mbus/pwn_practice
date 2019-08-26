2019.08.26(mon)

<pre><code>
#include <stdio.h>
#include <string.h>

int filter(char *cmd){
	int r=0;
	r += strstr(cmd, "flag")!=0;
	r += strstr(cmd, "sh")!=0;
	r += strstr(cmd, "tmp")!=0;
	return r;
}
int main(int argc, char* argv[], char** envp){
	putenv("PATH=/thankyouverymuch");
	if(filter(argv[1])) return 0;
	system( argv[1] );
	return 0;
}
</code></pre> 


#PATH environment 관련 문제
putenv 를 통해 path=/thankyouverymuch 를 환경변수 설정
/thankyouverymuch라는 폴더가 있는지 확인하였지만 폴더는 없음.
따라서 path 환경변수가 아무것도 없기 때문에 cat 명령어를 사용하기 위해서는
cat의 전체 경로를 입력해야함 /bin/cat

filter 에서 flag, sh, tmp 관련 단어가 들어가는지 체크하기 때문에 이를 우회하면서
flag 를 볼 수 있는 방법을 찾아봐야함.

./cmd1 "/bin/cat f*" 를 입력하여 문제 해결!

