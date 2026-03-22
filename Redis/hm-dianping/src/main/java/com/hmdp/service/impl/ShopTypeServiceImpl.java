package com.hmdp.service.impl;

import cn.hutool.core.util.StrUtil;
import cn.hutool.json.JSONUtil;
import com.hmdp.dto.Result;
import com.hmdp.entity.Shop;
import com.hmdp.entity.ShopType;
import com.hmdp.mapper.ShopTypeMapper;
import com.hmdp.service.IShopTypeService;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import org.springframework.data.redis.core.StringRedisTemplate;
import org.springframework.stereotype.Service;

import javax.annotation.Resource;
import java.util.List;

import static com.hmdp.utils.RedisConstants.CACHE_SHOP_TYPE_LIST_KEY;

/**
 * <p>
 *  服务实现类
 * </p>
 *
 * @author 虎哥
 * @since 2021-12-22
 */
@Service
public class ShopTypeServiceImpl extends ServiceImpl<ShopTypeMapper, ShopType> implements IShopTypeService {

    @Resource
    private StringRedisTemplate stringRedisTemplate;
    @Resource
    private ShopTypeMapper shopTypeMapper;

    @Override
    public List<ShopType> queryTypeList() {
        String key = CACHE_SHOP_TYPE_LIST_KEY;
        String shopTypeList = stringRedisTemplate.opsForValue().get(key);
        if (StrUtil.isNotEmpty(shopTypeList)) {
            List<ShopType> typeList = JSONUtil.toList(shopTypeList, ShopType.class);
            return typeList;
        }
        List<ShopType> typeList = shopTypeMapper.selectList(null);
        if (typeList.isEmpty()) {
            throw new RuntimeException("商铺类型错误");
        }
        stringRedisTemplate.opsForValue().set(key, JSONUtil.toJsonStr(typeList));
        return typeList;
    }
}
