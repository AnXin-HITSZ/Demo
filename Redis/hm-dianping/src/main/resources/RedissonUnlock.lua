local key = KEYS[1];	-- 锁的 key
local threadId = ARGV[1];	-- 线程唯一标识
local releaseTime = ARGV[2];	-- 锁的自动释放时间
-- 判断当前锁是否还是被自己持有
if (redis.call('HEXISTS', key, threadId) == 0) then
	return nil;	-- 如果已经不是自己，则直接返回
end;
-- 是自己的锁，则重入次数 - 1
local count = redis.call('HINCRBY', key, threadId, -1);
-- 判断重入次数是否已经为 0
if (count > 0) then
-- 大于 0 说明不能释放锁，重置有效期然后返回
	redis.call('EXPIRE', key, releaseTime);
	return nil;
else	-- 等于 0 说明可以释放锁，直接删除
	redis.call('DEL', key);
	return nil;
end;local key = KEYS[1];	-- 锁的 key
local threadId = ARGV[1];	-- 线程唯一标识
local releaseTime = ARGV[2];	-- 锁的自动释放时间
-- 判断当前锁是否还是被自己持有
if (redis.call('HEXISTS', key, threadId) == 0) then
	return nil;	-- 如果已经不是自己，则直接返回
end;
-- 是自己的锁，则重入次数 - 1
local count = redis.call('HINCRBY', key, threadId, -1);
-- 判断重入次数是否已经为 0
if (count > 0) then
-- 大于 0 说明不能释放锁，重置有效期然后返回
	redis.call('EXPIRE', key, releaseTime);
	return nil;
else	-- 等于 0 说明可以释放锁，直接删除
	redis.call('DEL', key);
	return nil;
end;