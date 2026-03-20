package com.anxin_hitsz;

import com.anxin_hitsz.util.JedisConnectionFactory;
import junit.extensions.TestSetup;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import redis.clients.jedis.Jedis;

import java.util.Map;

/**
 * ClassName: JedisTest
 * Package: com.anxin_hitsz
 * Description:
 *
 * @Author AnXin
 * @Create 2026/3/20 21:02
 * @Version 1.0
 */
public class JedisTest {
    private Jedis jedis;

    @BeforeEach
    void setUp() {
        // 1. 建立连接
//        jedis = new Jedis("8.135.60.136", 6379);
        jedis = JedisConnectionFactory.getJedis();
        // 2. 设置密码
        jedis.auth("AnXin517985!");
        // 3. 选择库
        jedis.select(0);
    }

    @Test
    public void testString() {
        // 存入数据
        String result = jedis.set("name", "Tom");
        System.out.println("result: " + result);
        // 获取数据
        String name = jedis.get("name");
        System.out.println("name: " + name);
    }

    @Test
    public void testHash() {
        // 插入 Hash 数据
        jedis.hset("user:1", "name", "Jack");
        jedis.hset("user:1", "age", "21");
        // 获取
        Map<String, String> map = jedis.hgetAll("user:1");
        System.out.println("map: " + map);
    }

    @AfterEach
    void tearDown() {
        if (jedis != null) {
            jedis.close();
        }
    }
}
