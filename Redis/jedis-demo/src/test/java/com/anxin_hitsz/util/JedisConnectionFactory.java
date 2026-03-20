package com.anxin_hitsz.util;

import redis.clients.jedis.Jedis;
import redis.clients.jedis.JedisPool;
import redis.clients.jedis.JedisPoolConfig;

/**
 * ClassName: JedisConnectionFactory
 * Package: com.anxin_hitsz.util
 * Description:
 *
 * @Author AnXin
 * @Create 2026/3/20 21:29
 * @Version 1.0
 */
public class JedisConnectionFactory {
    private static final JedisPool jedisPool;

    static {
        // 配置连接池
        JedisPoolConfig poolConfig = new JedisPoolConfig();
        poolConfig.setMaxTotal(8); // 最大连接数
        poolConfig.setMaxIdle(8);  // 最大空闲连接数
        poolConfig.setMinIdle(0);  // 最小空闲连接
        poolConfig.setMaxWaitMillis(1000);
        // 创建连接池对象
        jedisPool = new JedisPool(poolConfig, "8.135.60.136",
                6379, 1000, "AnXin517985!");
    }

    public static Jedis getJedis() {
        return jedisPool.getResource();
    }
}
