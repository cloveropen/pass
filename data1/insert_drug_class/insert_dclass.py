import asyncio

import motor.motor_asyncio

db_uri = "mongodb://drug:eastwillpass58@121.36.48.65:27017/drug"
db_conn_args = {
    "zlibCompressionLevel": 7,
    "compressors": "zlib"
}

# 连接数据库
def conn_mongo(db_uri:str,db_conn_args):
    client = motor.motor_asyncio.AsyncIOMotorClient(db_uri, **db_conn_args)
    db = client.get_database("drug")
    return db

# 插入一级分类
async def insert_class1():
    db = conn_mongo(db_uri,db_conn_args)
    await db.class1.drop()
    document = [
        {'code': '01', 'cname': '化学药品和生物制品'},
        {'code': '02', 'cname': '中成药'},
        {'code': '03', 'cname': '中药饮片'},
    ]
    result = await db.class1.insert_many(document)
    print('inserted %d docs' % (len(result.inserted_ids),))
    print('insert class1 success')

# 插入二级分类
async def insert_class2():
    db = conn_mongo(db_uri,db_conn_args)
    await db.class2.drop()
    document = [
        {'code': '0101', 'cname': '抗微生物药'},
        {'code': '0102', 'cname': '抗寄生虫药'},
        {'code': '0103', 'cname': '麻醉药'},
        {'code': '0104', 'cname': '镇痛、解热、抗炎、抗风湿、抗痛风药'},
        {'code': '0105', 'cname': '神经系统用药'},
        {'code': '0106', 'cname': '之类精神障碍药'},
        {'code': '0107', 'cname': '心血管系统用药'},
        {'code': '0108', 'cname': '呼吸系统用药'},
        {'code': '0109', 'cname': '消化系统用药'},
        {'code': '0110', 'cname': '泌尿系统用药'},
        {'code': '0111', 'cname': '血液系统用药'},
        {'code': '0112', 'cname': '激素及影响内分泌药'},
        {'code': '0113', 'cname': '抗变态反应药'},
        {'code': '0114', 'cname': '免疫系统用药'},
        {'code': '0115', 'cname': '抗肿瘤药'},
        {'code': '0116', 'cname': '维生素、矿物质类药'},
        {'code': '0117', 'cname': '调节水、电解质及酸碱平衡药'},
        {'code': '0118', 'cname': '解毒药'},
        {'code': '0119', 'cname': '生物制品'},
        {'code': '0120', 'cname': '诊断用药'},
        {'code': '0121', 'cname': '皮肤科用药'},
        {'code': '0122', 'cname': '眼科用药'},
        {'code': '0123', 'cname': '耳鼻喉科用药'},
        {'code': '0124', 'cname': '妇产科用药'},
        {'code': '0125', 'cname': '计划生育用药'},
        {'code': '0201', 'cname': '内科用药'},
        {'code': '0202', 'cname': '外科用药'},
        {'code': '0203', 'cname': '妇科用药'},
        {'code': '0204', 'cname': '眼科用药'},
        {'code': '0205', 'cname': '耳鼻喉科用药'},
        {'code': '0206', 'cname': '骨伤科用药'},
    ]
    result = await db.class2.insert_many(document)
    print('inserted %d docs' % (len(result.inserted_ids),))
    print('insert class2 success')

# 插入三级分类
async def insert_class3():
    db = conn_mongo(db_uri,db_conn_args)
    await db.class3.drop()
    document = [
        {'code': '010101', 'cname': '青霉素类'},
        {'code': '010102', 'cname': '头孢菌素类'},
        {'code': '010103', 'cname': '氨基糖苷类'},
        {'code': '010104', 'cname': '四环素类'},
        {'code': '010105', 'cname': '大环内酯类'},
        {'code': '010106', 'cname': '其他抗生素'},
        {'code': '010107', 'cname': '磺胺类'},
        {'code': '010108', 'cname': '喹诺酮类'},
        {'code': '010109', 'cname': '硝基咪唑类'},
        {'code': '010110', 'cname': '硝基呋喃类'},
        {'code': '010111', 'cname': '抗结核病药'},
        {'code': '010112', 'cname': '抗麻风病药'},
        {'code': '010113', 'cname': '抗真菌药'},
        {'code': '010114', 'cname': '抗病毒药'},
        {'code': '010201', 'cname': '抗疟药'},
        {'code': '010202', 'cname': '抗阿米巴并药及抗滴虫病药'},
        {'code': '010203', 'cname': '抗利士曼原虫药'},
        {'code': '010204', 'cname': '抗血吸虫病药'},
        {'code': '010205', 'cname': '驱肠虫药'},
        {'code': '010301', 'cname': '局部麻醉药'},
        {'code': '010302', 'cname': '全身麻醉药'},
        {'code': '010303', 'cname': '麻醉辅助药'},
        {'code': '010401', 'cname': '镇痛药'},
        {'code': '010402', 'cname': '解热镇痛、抗炎、抗风湿药'},
        {'code': '010403', 'cname': '抗痛风药'},
        {'code': '010501', 'cname': '抗震颤麻痹药'},
        {'code': '010502', 'cname': '抗重症肌无力药'},
        {'code': '010503', 'cname': '抗癫痫药'},
        {'code': '010504', 'cname': '脑血管病用药及降颅压药'},
        {'code': '010505', 'cname': '中枢兴奋药'},
        {'code': '010506', 'cname': '抗痴呆药'},
        {'code': '010601', 'cname': '抗精神病药'},
        {'code': '010602', 'cname': '抗抑郁药'},
        {'code': '010603', 'cname': '抗焦虑药'},
        {'code': '010604', 'cname': '抗躁狂药'},
        {'code': '010605', 'cname': '镇静催眠药'},
        {'code': '010701', 'cname': '抗心绞痛药'},
        {'code': '010702', 'cname': '抗心律失常药'},
        {'code': '010703', 'cname': '抗心力衰竭药'},
        {'code': '010704', 'cname': '抗高血压药'},
        {'code': '010705', 'cname': '抗休克药'},
        {'code': '010706', 'cname': '调脂及抗动脉粥样硬化药'},
        {'code': '010801', 'cname': '抗痰药'},
        {'code': '010802', 'cname': '镇咳药'},
        {'code': '010803', 'cname': '平喘药'},
        {'code': '010901', 'cname': '抗酸药及抗溃疡病药'},
        {'code': '010902', 'cname': '助消化药'},
        {'code': '010903', 'cname': '胃肠解痉药及胃动力药'},
        {'code': '010904', 'cname': '泻药及止泻药'},
        {'code': '010905', 'cname': '肝病辅助治疗药'},
        {'code': '010906', 'cname': '微生态制剂'},
        {'code': '010907', 'cname': '利胆药'},
        {'code': '010908', 'cname': '治疗炎性肠病药'},
        {'code': '011001', 'cname': '利尿药'},
        {'code': '011002', 'cname': '良性前列腺增生用药'},
        {'code': '011101', 'cname': '抗贫血药'},
        {'code': '011102', 'cname': '抗血小板药'},
        {'code': '011103', 'cname': '促凝血药'},
        {'code': '011104', 'cname': '抗凝血药及溶栓药'},
        {'code': '011105', 'cname': '血管量扩充剂'},
        {'code': '011201', 'cname': '下丘脑垂体激素及其类似物'},
        {'code': '011202', 'cname': '肾上腺皮质激素类药'},
        {'code': '011203', 'cname': '胰岛素及口服降血糖药'},
        {'code': '011204', 'cname': '甲状腺激素及抗甲状腺药'},
        {'code': '011205', 'cname': '雄激素及同化激素'},
        {'code': '011206', 'cname': '雌激素、孕激素及抗孕激素'},
        {'code': '011207', 'cname': '钙代谢调节药及抗骨质疏松药'},
        {'code': '011301', 'cname': '抗变态反应药'},
        {'code': '011401', 'cname': '免疫系统用药'},
        {'code': '011501', 'cname': '烷化剂'},
        {'code': '011502', 'cname': '抗代谢药'},
        {'code': '011503', 'cname': '抗肿瘤抗生素'},
        {'code': '011504', 'cname': '抗肿瘤植物成分药'},
        {'code': '011505', 'cname': '其他抗肿瘤药'},
        {'code': '011506', 'cname': '抗肿瘤激素类'},
        {'code': '011507', 'cname': '抗肿瘤辅助药'},
        {'code': '011601', 'cname': '维生素'},
        {'code': '011602', 'cname': '矿物质'},
        {'code': '011603', 'cname': '肠外营养药'},
        {'code': '011701', 'cname': '水、电解质平衡调节药'},
        {'code': '011702', 'cname': '酸碱平衡调节药'},
        {'code': '011703', 'cname': '其他'},
        {'code': '011801', 'cname': '氰化物中毒解毒药'},
        {'code': '011802', 'cname': '有机磷酸酯类中毒解毒药'},
        {'code': '011803', 'cname': '亚硝酸盐中毒解毒药'},
        {'code': '011804', 'cname': '阿片类中毒解毒药'},
        {'code': '011805', 'cname': '其他'},
        {'code': '011901', 'cname': '生物制品'},
        {'code': '012001', 'cname': '造影剂'},
        {'code': '012002', 'cname': '其他'},
        {'code': '012101', 'cname': '抗感染药'},
        {'code': '012102', 'cname': '角膜溶解药'},
        {'code': '012103', 'cname': '肾上腺皮质激素类药'},
        {'code': '012104', 'cname': '其他'},
        {'code': '012201', 'cname': '抗感染药'},
        {'code': '012202', 'cname': '青光眼用药'},
        {'code': '012203', 'cname': '其他'},
        {'code': '012301', 'cname': '耳鼻喉科用药'},
        {'code': '012401', 'cname': '子宫收缩药'},
        {'code': '012402', 'cname': '其他'},
        {'code': '012501', 'cname': '计划生育用药'},
        {'code': '020101', 'cname': '解表剂'},
        {'code': '020102', 'cname': '泻下剂'},
        {'code': '020103', 'cname': '清热剂'},
        {'code': '020104', 'cname': '温里剂'},
        {'code': '020105', 'cname': '化痰、止咳、平喘剂'},
        {'code': '020106', 'cname': '开窍剂'},
        {'code': '020107', 'cname': '扶正剂'},
        {'code': '020108', 'cname': '安神剂'},
        {'code': '020109', 'cname': '止血剂'},
        {'code': '020110', 'cname': '被淤剂'},
        {'code': '020111', 'cname': '理气剂'},
        {'code': '020112', 'cname': '消导剂'},
        {'code': '020113', 'cname': '治风剂'},
        {'code': '020114', 'cname': '被湿剂'},
        {'code': '020115', 'cname': '调脂剂'},
        {'code': '020116', 'cname': '固涩剂'},
        {'code': '020201', 'cname': '清热剂'},
        {'code': '020202', 'cname': '温经理气活血剂'},
        {'code': '020203', 'cname': '活血化瘀剂'},
        {'code': '020301', 'cname': '理血剂'},
        {'code': '020302', 'cname': '清热剂'},
        {'code': '020303', 'cname': '扶正剂'},
        {'code': '020304', 'cname': '散结剂'},
        {'code': '020401', 'cname': '清热剂'},
        {'code': '020402', 'cname': '扶正剂'},
        {'code': '020501', 'cname': '耳病'},
        {'code': '020502', 'cname': '鼻病'},
        {'code': '020503', 'cname': '咽喉、口腔病'},
        {'code': '020601', 'cname': '接骨续筋'},
        {'code': '020602', 'cname': '活血化瘀'},
        {'code': '020603', 'cname': '活血通络'},
        {'code': '020604', 'cname': '祛风活络'},
        {'code': '020605', 'cname': '补肾壮骨'},
    ]
    result = await db.class3.insert_many(document)
    print('inserted %d docs' % (len(result.inserted_ids),))
    print('insert class3 success')

async def main():
    await insert_class1()
    await insert_class2()
    await insert_class3()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())