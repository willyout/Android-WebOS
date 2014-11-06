#include "config.h" 
#include "HelloObject.h"

#define THE_DEVICE "/sys/class/timed_output/vibrator/enable"
#define O_RDWR		00000002

namespace WebCore {

	HelloObject::HelloObject() { }

	String HelloObject::sayHello() const { 
		return "Hello World from WebKit !" ;
	}

	String HelloObject::getOneMess(){
		if(mess.empty())
			return "empty";
		String m = (String)mess.front();
		mess.pop();
		return m;
	}
	
	String HelloObject::getOneMess2(){
		return HelloObject::getOneMess();
	}
	
	void HelloObject::addOneMess(String m){
		mess.push(m);
	}
	
	int HelloObject::vibrate(int timeout_ms){
		int nwr, ret, fd;
		char value[20];
		fd = open(THE_DEVICE, O_RDWR);
		if(fd < 0)
			return 0;
		
		nwr = sprintf(value, "%d\n", timeout_ms);
		ret = write(fd, value, nwr);
		close(fd);
		return timeout_ms;
	}
	
	int HelloObject::sleep(int times){
		sleep(times);
    	return times;
	}
} // namespace WebCore