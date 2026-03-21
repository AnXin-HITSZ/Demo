package com.anxin_hitsz.redis.pojo;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

/**
 * ClassName: User
 * Package: com.anxin_hitsz.redis.pojo
 * Description:
 *
 * @Author AnXin
 * @Create 2026/3/21 13:28
 * @Version 1.0
 */
@Data
@NoArgsConstructor
@AllArgsConstructor
public class User {
    private String name;
    private Integer age;
}
