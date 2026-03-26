package com.hmdp;

import org.junit.jupiter.api.BeforeEach;
import org.redisson.api.RLock;
import org.redisson.api.RedissonClient;

import javax.annotation.Resource;

/**
 * ClassName: RedissonTest
 * Package: com.hmdp
 * Description:
 *
 * @Author AnXin
 * @Create 2026/3/26 11:47
 * @Version 1.0
 */
public class RedissonTest {

    @Resource
    private RedissonClient redissonClient1;
    @Resource
    private RedissonClient redissonClient2;
    @Resource
    private RedissonClient redissonClient3;

    private RLock lock;

    @BeforeEach
    void setUp() {
        RLock lock1 = redissonClient1.getLock("order");
        RLock lock2 = redissonClient2.getLock("order");
        RLock lock3 = redissonClient3.getLock("order");

        // 创建联锁 multiLock
        lock = redissonClient1.getMultiLock(lock1, lock2, lock3);
    }
}
