# 变量定义 - 未指定类型注解 -> 类型推断

# 变量定义 - 指定类型注解
a: int = 596
score: float = 98.5
hobby: str = "Python"
flag: bool = True
none: None = None

lists: list[str | int] = ["A", "B", "C"]
sets: set[str] = {"123", "456", "789"}
dicts: dict[str, int] = {"str_01": 1, "str_02": 2}
tuples: tuple[str, int, int] = ("tuple", 1, 2)

lists.append("D")
lists.append(10)
lists.append(10.0)

# 函数类型注解
def circle_area_len(r: float) -> tuple[float, float]:
    return round(3.14 * r * r, 1), round(2 * 3.14 * r, 1)

al = circle_area_len(8.5)
print(al)

def calc_order_cost(*args: tuple[str, float, int], coupon: int=0, score: int=0, express: float=0.0) -> float:
    """
    根据传入的一批商品信息（商品名、价格、数量）、优惠（优惠券、积分抵扣）、运费信息计算订单的总金额
    :param args: 商品信息（商品名、价格、数量）
    :param coupon: 优惠券
    :param score: 积分
    :param express: 运费
    :return: 订单的总金额
    """
    # 订单的总金额 = 商品总金额 - 优惠券 - 积分抵扣 + 运费
    # 1. 计算商品总金额
    total_price = [goods[1] * goods[2] for goods in args]
    total_cost = sum(total_price)

    # 2. 扣减优惠券
    if total_cost >= 5000 and coupon <= total_cost:
        total_cost -= coupon

    # 3. 扣减积分抵扣
    if total_cost >= 5000 and score // 100 <= total_cost:
        total_cost -= score // 100

    # 4. 添加运费
    total_cost += express

    return total_cost

# 测试

total = calc_order_cost(("good_1", 188, 2), ("goods_2", 388, 1), ("goods_3", 6999, 1))
print(total)
