package com.anxin_hitsz;

import com.anxin_hitsz.redis.pojo.User;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.data.redis.core.RedisTemplate;

@SpringBootTest
class SpringdataRedisDemoApplicationTests {

    @Autowired
    private RedisTemplate<String, Object> redisTemplate;

    @Test
    void contextLoads() {
        // 写入一条 String 数据
        redisTemplate.opsForValue().set("name", "Jerry");
        // 获取 String 数据
        Object name = redisTemplate.opsForValue().get("name");
        System.out.println("name = " + name);
    }

    @Test
    void testSaveUser() {
        // 写入数据
        redisTemplate.opsForValue().set("user:100", new User("Jerry", 21));
        // 获取数据
        User o = (User) redisTemplate.opsForValue().get("user:100");

        System.out.println("o = " + o);
    }

}
