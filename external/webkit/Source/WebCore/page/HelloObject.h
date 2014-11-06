#ifndef HelloObject_h 
#define HelloObject_h
#include <wtf/PassRefPtr.h> 
#include <wtf/RefCounted.h>

#include <queue>
#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#include <errno.h>
#include "PlatformString.h"

namespace WebCore {

    class HelloObject : public RefCounted<HelloObject> { 
    public: 
        static PassRefPtr<HelloObject> create() { return adoptRef(new HelloObject()); }
        String sayHello() const;
        String getOneMess();
        String getOneMess2();
        void addOneMess(String m);
        int vibrate(int timeout_ms);
        int sleep(int times);
    private: 
        HelloObject();   
        std::queue<String> mess;        
    };

} // namespace WebCore
#endif // HelloObject_h