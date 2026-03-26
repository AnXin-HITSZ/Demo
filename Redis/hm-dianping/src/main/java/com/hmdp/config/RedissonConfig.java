package com.hmdp.config;

import org.redisson.Redisson;
import org.redisson.api.RedissonClient;
import org.redisson.config.Config;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

/**
 * ClassName: RedissonConfig
 * Package: com.hmdp.config
 * Description:
 *
 * @Author AnXin
 * @Create 2026/3/25 20:10
 * @Version 1.0
 */
@Configuration
public class RedissonConfig {

    @Bean
    public RedissonClient redissonClient1() {
        // 配置类
        Config config = new Config();
        // 添加 Redis 地址，这里添加了单点的地址，也可以使用 config.useClusterServers() 添加集群地址
        config.useSingleServer().setAddress("redis://8.135.60.136:6379").setPassword("AnXin517985!");
        // 创建客户端
        return Redisson.create(config);
    }

    @Bean
    public RedissonClient redissonClient2() {
        // 配置类
        Config config = new Config();
        // 添加 Redis 地址，这里添加了单点的地址，也可以使用 config.useClusterServers() 添加集群地址
        config.useSingleServer().setAddress("redis://8.135.60.136:6379").setPassword("AnXin517985!");
        // 创建客户端
        return Redisson.create(config);
    }

    @Bean
    public RedissonClient redissonClient3() {
        // 配置类
        Config config = new Config();
        // 添加 Redis 地址，这里添加了单点的地址，也可以使用 config.useClusterServers() 添加集群地址
        config.useSingleServer().setAddress("redis://8.135.60.136:6379").setPassword("AnXin517985!");
        // 创建客户端
        return Redisson.create(config);
    }
}
