package com.hmdp.service;

/**
 * ClassName: ILock
 * Package: com.hmdp.service
 * Description:
 *
 * @Author AnXin
 * @Create 2026/3/25 14:26
 * @Version 1.0
 */
public interface ILock {

    /**
     * 尝试获取锁
     * @param timeoutSec 锁持有的超时时间，过期后自动释放
     * @return true 代表获取锁成功，false 代表获取锁失败
     */
    boolean tryLock(long timeoutSec);

    /**
     * 释放锁
     */
    void unlock();
}
