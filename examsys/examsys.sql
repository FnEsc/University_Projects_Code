/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 50617
Source Host           : localhost:3306
Source Database       : examsys

Target Server Type    : MYSQL
Target Server Version : 50617
File Encoding         : 65001

Date: 2019-04-13 20:40:49
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for adqm
-- ----------------------------
DROP TABLE IF EXISTS `adqm`;
CREATE TABLE `adqm` (
  `mid` int(11) NOT NULL AUTO_INCREMENT,
  `mowneruid` int(11) NOT NULL,
  `qmtitle` varchar(255) NOT NULL,
  `qmdescribe` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`mid`),
  KEY `owneruid` (`mowneruid`),
  CONSTRAINT `adqm_ibfk_1` FOREIGN KEY (`mowneruid`) REFERENCES `userinfo` (`uid`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of adqm
-- ----------------------------
INSERT INTO `adqm` VALUES ('1', '1', '管理员1题目模块1', '题目1-4');
INSERT INTO `adqm` VALUES ('2', '1', '管理员1题目模块2', '题目3-5');
INSERT INTO `adqm` VALUES ('3', '5', '管理员11题目模块1', '题目1-5（qid是6-10）');

-- ----------------------------
-- Table structure for examinfo
-- ----------------------------
DROP TABLE IF EXISTS `examinfo`;
CREATE TABLE `examinfo` (
  `exid` int(11) NOT NULL AUTO_INCREMENT COMMENT '问卷序号',
  `creater` int(11) DEFAULT NULL,
  `createtime` datetime DEFAULT NULL,
  `mid` int(11) DEFAULT NULL,
  `extitle` varchar(255) DEFAULT NULL,
  `exdescribe` varchar(255) DEFAULT NULL,
  `op1` int(11) DEFAULT NULL COMMENT '顺序随机 1随机 2固定',
  `op2` int(11) DEFAULT NULL COMMENT '问卷题目数量',
  `op3` int(11) DEFAULT NULL COMMENT 'ABCD选择随机',
  `op4` int(11) DEFAULT NULL COMMENT '答题时间限定 单位 秒',
  `op5` int(11) DEFAULT NULL COMMENT '是否允许空卷',
  `op6` datetime DEFAULT NULL COMMENT '开始时间',
  `op7` datetime DEFAULT NULL COMMENT '结束时间',
  PRIMARY KEY (`exid`),
  KEY `creater` (`creater`),
  KEY `mid` (`mid`),
  CONSTRAINT `examinfo_ibfk_1` FOREIGN KEY (`creater`) REFERENCES `userinfo` (`uid`) ON DELETE CASCADE,
  CONSTRAINT `examinfo_ibfk_2` FOREIGN KEY (`mid`) REFERENCES `adqm` (`mid`) ON DELETE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of examinfo
-- ----------------------------
INSERT INTO `examinfo` VALUES ('1', '1', '2019-02-19 19:57:31', '1', '问卷1', '管理员1问卷1借用题目模块1', '0', '4', '0', '0', '0', '2019-02-19 19:59:53', '2026-02-10 19:59:59');
INSERT INTO `examinfo` VALUES ('2', '1', '2019-02-21 20:52:27', '2', '问卷2', '管理员1问卷2借用题目模块2', '0', '2', '1', '0', '0', '2019-04-01 19:36:24', '2059-04-13 19:36:28');

-- ----------------------------
-- Table structure for examrecord
-- ----------------------------
DROP TABLE IF EXISTS `examrecord`;
CREATE TABLE `examrecord` (
  `erid` int(11) NOT NULL AUTO_INCREMENT COMMENT '问卷记录序号',
  `creater` int(11) DEFAULT NULL,
  `exid` int(11) DEFAULT NULL COMMENT '问卷序号',
  `auid` int(11) DEFAULT NULL COMMENT '答题用户',
  `answertime` datetime DEFAULT NULL,
  PRIMARY KEY (`erid`),
  KEY `creater` (`creater`),
  KEY `exid` (`exid`),
  KEY `auid` (`auid`) USING BTREE,
  CONSTRAINT `examrecord_ibfk_3` FOREIGN KEY (`auid`) REFERENCES `userrely` (`slaveuid`) ON DELETE CASCADE,
  CONSTRAINT `examrecord_ibfk_1` FOREIGN KEY (`creater`) REFERENCES `examinfo` (`creater`) ON DELETE CASCADE,
  CONSTRAINT `examrecord_ibfk_2` FOREIGN KEY (`exid`) REFERENCES `examinfo` (`exid`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of examrecord
-- ----------------------------
INSERT INTO `examrecord` VALUES ('1', '1', '1', '2', '2019-04-18 19:56:17');
INSERT INTO `examrecord` VALUES ('2', '1', '2', '11', '2019-04-13 19:56:10');

-- ----------------------------
-- Table structure for groupinfo
-- ----------------------------
DROP TABLE IF EXISTS `groupinfo`;
CREATE TABLE `groupinfo` (
  `gid` int(11) NOT NULL AUTO_INCREMENT,
  `gowneruid` int(11) DEFAULT NULL,
  `gtitle` varchar(255) DEFAULT NULL COMMENT '组名 管理员自定义',
  `gdescribe` varchar(255) DEFAULT NULL COMMENT '组描述 管理员自定义',
  PRIMARY KEY (`gid`),
  KEY `gowneruid` (`gowneruid`),
  CONSTRAINT `groupinfo_ibfk_1` FOREIGN KEY (`gowneruid`) REFERENCES `userinfo` (`uid`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of groupinfo
-- ----------------------------
INSERT INTO `groupinfo` VALUES ('1', '1', '管理员1组1', '设置为2~4');
INSERT INTO `groupinfo` VALUES ('2', '1', '管理员1组2', '设置为5~9');
INSERT INTO `groupinfo` VALUES ('3', '5', '管理员11组1', '设置为12~14');

-- ----------------------------
-- Table structure for gusers
-- ----------------------------
DROP TABLE IF EXISTS `gusers`;
CREATE TABLE `gusers` (
  `gid` int(11) DEFAULT NULL,
  `gowneruid` int(11) NOT NULL,
  `guseruid` int(11) NOT NULL,
  PRIMARY KEY (`gowneruid`,`guseruid`),
  KEY `gid` (`gid`),
  KEY `guseruid` (`guseruid`),
  CONSTRAINT `gusers_ibfk_1` FOREIGN KEY (`gid`) REFERENCES `groupinfo` (`gid`) ON DELETE SET NULL,
  CONSTRAINT `gusers_ibfk_2` FOREIGN KEY (`gowneruid`) REFERENCES `groupinfo` (`gowneruid`) ON DELETE CASCADE,
  CONSTRAINT `gusers_ibfk_3` FOREIGN KEY (`guseruid`) REFERENCES `userrely` (`slaveuid`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of gusers
-- ----------------------------
INSERT INTO `gusers` VALUES ('1', '1', '2');
INSERT INTO `gusers` VALUES ('1', '1', '3');
INSERT INTO `gusers` VALUES ('1', '1', '4');
INSERT INTO `gusers` VALUES ('2', '1', '9');
INSERT INTO `gusers` VALUES ('2', '1', '10');
INSERT INTO `gusers` VALUES ('2', '1', '11');
INSERT INTO `gusers` VALUES ('2', '1', '12');
INSERT INTO `gusers` VALUES ('2', '1', '13');
INSERT INTO `gusers` VALUES ('3', '5', '6');
INSERT INTO `gusers` VALUES ('3', '5', '7');
INSERT INTO `gusers` VALUES ('3', '5', '8');

-- ----------------------------
-- Table structure for history
-- ----------------------------
DROP TABLE IF EXISTS `history`;
CREATE TABLE `history` (
  `hid` int(11) NOT NULL AUTO_INCREMENT,
  `erid` int(11) DEFAULT NULL,
  `qid` int(11) DEFAULT NULL,
  `a` varchar(300) DEFAULT NULL,
  `selected` varchar(300) DEFAULT NULL,
  `answerbool` int(11) DEFAULT NULL COMMENT '答题对错',
  PRIMARY KEY (`hid`),
  KEY `erid` (`erid`),
  KEY `history_ibfk_2` (`qid`),
  CONSTRAINT `history_ibfk_1` FOREIGN KEY (`erid`) REFERENCES `examrecord` (`erid`) ON DELETE CASCADE,
  CONSTRAINT `history_ibfk_2` FOREIGN KEY (`qid`) REFERENCES `questions` (`qid`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of history
-- ----------------------------
INSERT INTO `history` VALUES ('1', '1', '1', '2', '1', '0');
INSERT INTO `history` VALUES ('2', '1', '3', '1234', '12', '0');
INSERT INTO `history` VALUES ('3', '1', '4', '234', '234', '1');
INSERT INTO `history` VALUES ('4', '1', '2', '3', '3', '1');
INSERT INTO `history` VALUES ('5', '2', '3', '1234', '1234', '1');
INSERT INTO `history` VALUES ('6', '2', '5', '1', '2', '0');

-- ----------------------------
-- Table structure for qtom
-- ----------------------------
DROP TABLE IF EXISTS `qtom`;
CREATE TABLE `qtom` (
  `mid` int(11) DEFAULT NULL,
  `qid` int(11) DEFAULT NULL,
  KEY `mid` (`mid`),
  KEY `qid` (`qid`),
  CONSTRAINT `qtom_ibfk_1` FOREIGN KEY (`mid`) REFERENCES `adqm` (`mid`) ON DELETE CASCADE,
  CONSTRAINT `qtom_ibfk_2` FOREIGN KEY (`qid`) REFERENCES `questions` (`qid`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of qtom
-- ----------------------------
INSERT INTO `qtom` VALUES ('1', '1');
INSERT INTO `qtom` VALUES ('1', '2');
INSERT INTO `qtom` VALUES ('1', '3');
INSERT INTO `qtom` VALUES ('1', '4');
INSERT INTO `qtom` VALUES ('2', '3');
INSERT INTO `qtom` VALUES ('2', '4');
INSERT INTO `qtom` VALUES ('2', '5');
INSERT INTO `qtom` VALUES ('3', '6');
INSERT INTO `qtom` VALUES ('3', '7');
INSERT INTO `qtom` VALUES ('3', '8');
INSERT INTO `qtom` VALUES ('3', '9');
INSERT INTO `qtom` VALUES ('3', '10');

-- ----------------------------
-- Table structure for questions
-- ----------------------------
DROP TABLE IF EXISTS `questions`;
CREATE TABLE `questions` (
  `qid` int(11) NOT NULL AUTO_INCREMENT,
  `qtpye` int(11) DEFAULT NULL COMMENT '题目类型 1单选 2多选 3判断',
  `q` varchar(1000) DEFAULT NULL,
  `a` int(11) DEFAULT NULL COMMENT '1234的答案形式',
  `op1` varchar(300) DEFAULT NULL,
  `op2` varchar(300) DEFAULT NULL,
  `op3` varchar(300) DEFAULT NULL,
  `op4` varchar(300) DEFAULT NULL,
  `qowneruid` int(11) DEFAULT NULL,
  `amount` int(11) DEFAULT NULL,
  `acamount` int(11) DEFAULT NULL,
  `qacrate` float DEFAULT NULL,
  PRIMARY KEY (`qid`),
  KEY `owneruid` (`qowneruid`),
  CONSTRAINT `questions_ibfk_1` FOREIGN KEY (`qowneruid`) REFERENCES `userinfo` (`uid`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of questions
-- ----------------------------
INSERT INTO `questions` VALUES ('1', '1', '入户拜访的6步骤中属于第4步的是？', '2', '预约沟通', '持续关怀', '适时销售', '提高粘度', '1', '0', '0', '0');
INSERT INTO `questions` VALUES ('2', '1', '明明妈妈是店里顾客，但是宝宝一直吃母乳，你对母乳顾客的服务是：每月至少一条育儿短信，3个月电话跟进一次，至少到宝宝几岁？\r\n明明妈妈是店里顾客，但是宝宝一直吃母乳，你对母乳顾客的服务是：每月至少一条育儿短信，3个月电话跟进一次，至少到宝宝几岁？', '3', '3岁', '1岁', '2岁', '半岁', '1', '0', '0', '0');
INSERT INTO `questions` VALUES ('3', '2', '掌中宝“会员管理”中“我的会员”可以通过哪些内容进行筛选？', '1234', '全部会员（显示全部会员）、月龄分类、喂养类型、自定义分类', '产品分类、段位分类', '.注册时间、积分分类', '会员类型、会员级别', '1', '0', '0', '0');
INSERT INTO `questions` VALUES ('4', '2', '营养顾问在和顾客聊天时说到“圣元国际”，客户说：“圣元不是国产品牌吗？你怎么说是“圣元国际”呢？”请你给顾客介绍下圣元主要机构分布情况：', '234', '生产基地：在北京', '总部：在美国', '原料基地：在法国', '研发中心：在北京', '1', '0', '0', '0');
INSERT INTO `questions` VALUES ('5', '3', '圣元实验室的标准是CNAS国家级实验室', '1', '正确', '错误', null, null, '1', '0', '0', '0');
INSERT INTO `questions` VALUES ('6', '2', '华北营养顾问林立娜(入职8个月，坚持会员回访，月均回访率45%，7月袋鼠360增长奖金840元)分享：“耕耘就有收获，付出就有回报。”请问如何做好顾客回访？', '1234', '回访前的知识准备', '回访前的顾客名单整理', '真诚', '坚持做', '5', '0', '0', '0');
INSERT INTO `questions` VALUES ('7', '2', '电访的过程中，发现一位老客户因为促销活动的原因，转成了他牌客户。为了宝宝继续食用优博奶粉，你需要把优博奶粉与他牌进行比较。那么，如何与他牌比较呢？', '23', '拿对手的优势与自己的弱点做客观地比较', '不贬低对手', '强调自身的独特卖点', '贬低对手', '5', '0', '0', '0');
INSERT INTO `questions` VALUES ('8', '1', '标准销售动作主要是为了指导新顾问销售思路。一般标准的销售动作包含①接近顾客；②了解需求；③介绍产品；④处理异议；⑤促单成交；⑥关联销售；⑦相关服务。请问以下哪一步不是标准的销售动作？', '1', '助销促销', '介绍产品', '接近顾客', '关联销售', '5', '0', '0', '0');
INSERT INTO `questions` VALUES ('9', '3', '圣元的企业使命是：关爱中国婴幼儿的健康，专注提供优质的产品和服务，为妈妈、宝宝带来健康和快乐。圣元员工的做事原则是人人用心，人人卖力；', '1', '正确', '错误', null, null, '5', '0', '0', '0');
INSERT INTO `questions` VALUES ('10', '3', '客户购买后，在一周之内打第一次回访电话。', '2', '正确', '错误', null, null, '5', null, null, null);

-- ----------------------------
-- Table structure for suggestions
-- ----------------------------
DROP TABLE IF EXISTS `suggestions`;
CREATE TABLE `suggestions` (
  `sugid` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) DEFAULT NULL,
  `exid` int(11) DEFAULT NULL,
  `sugdescribe` varchar(255) DEFAULT NULL COMMENT '意见描述',
  PRIMARY KEY (`sugid`),
  KEY `uid` (`uid`),
  KEY `exid` (`exid`),
  CONSTRAINT `suggestions_ibfk_1` FOREIGN KEY (`uid`) REFERENCES `userinfo` (`uid`) ON DELETE CASCADE,
  CONSTRAINT `suggestions_ibfk_2` FOREIGN KEY (`exid`) REFERENCES `examinfo` (`exid`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of suggestions
-- ----------------------------
INSERT INTO `suggestions` VALUES ('1', '1', '1', 'sugid1这是管理员1uid1对exid1反馈的意见1。');
INSERT INTO `suggestions` VALUES ('2', '1', '1', 'sugid1这是管理员1uid1对exid1反馈的意见2。');
INSERT INTO `suggestions` VALUES ('3', '2', '1', 'sugid3这是用户2uid2对exid1反馈的意见。');
INSERT INTO `suggestions` VALUES ('4', '11', '2', 'sugid4这是用户7uid11对exid2反馈的意见。');

-- ----------------------------
-- Table structure for userinfo
-- ----------------------------
DROP TABLE IF EXISTS `userinfo`;
CREATE TABLE `userinfo` (
  `uid` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(20) NOT NULL COMMENT '邮箱格式',
  `password` varchar(32) NOT NULL COMMENT '密码、8-32位',
  `nickname` varchar(32) NOT NULL COMMENT '用户自定义昵称、可重复',
  `ismaster` int(10) unsigned zerofill DEFAULT NULL COMMENT '管理员1 用户0',
  PRIMARY KEY (`username`),
  KEY `uid` (`uid`),
  KEY `nickname` (`nickname`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of userinfo
-- ----------------------------
INSERT INTO `userinfo` VALUES ('5', '11@qq.com', '11', '用户昵称11', '0000000001');
INSERT INTO `userinfo` VALUES ('6', '12@qq.com', '12', '用户昵称12', '0000000000');
INSERT INTO `userinfo` VALUES ('7', '13@qq.com', '13', '用户昵称13', '0000000000');
INSERT INTO `userinfo` VALUES ('8', '14@qq.com', '14', '用户昵称14', '0000000000');
INSERT INTO `userinfo` VALUES ('1', '1@qq.com', '1', '用户昵称1', '0000000001');
INSERT INTO `userinfo` VALUES ('2', '2@qq.com', '2', '用户昵称2', '0000000000');
INSERT INTO `userinfo` VALUES ('3', '3@qq.com', '3', '用户昵称3', '0000000000');
INSERT INTO `userinfo` VALUES ('4', '4@qq.com', '4', '用户昵称4', '0000000000');
INSERT INTO `userinfo` VALUES ('9', '5@qq.com', '5', '用户昵称5', '0000000000');
INSERT INTO `userinfo` VALUES ('10', '6@qq.com', '6', '用户昵称6', '0000000000');
INSERT INTO `userinfo` VALUES ('11', '7@qq.com', '7', '用户昵称7', '0000000000');
INSERT INTO `userinfo` VALUES ('12', '8@qq.com', '8', '用户昵称8', '0000000000');
INSERT INTO `userinfo` VALUES ('13', '9@qq.com', '9', '用户昵称9', '0000000000');

-- ----------------------------
-- Table structure for userrely
-- ----------------------------
DROP TABLE IF EXISTS `userrely`;
CREATE TABLE `userrely` (
  `slaveuid` int(11) NOT NULL COMMENT '可一对多',
  `masteruid` int(11) NOT NULL,
  `acrate` float NOT NULL COMMENT '用户答题准确率',
  PRIMARY KEY (`slaveuid`,`masteruid`),
  KEY `masteruid` (`masteruid`),
  CONSTRAINT `userrely_ibfk_1` FOREIGN KEY (`slaveuid`) REFERENCES `userinfo` (`uid`) ON DELETE CASCADE,
  CONSTRAINT `userrely_ibfk_2` FOREIGN KEY (`masteruid`) REFERENCES `userinfo` (`uid`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of userrely
-- ----------------------------
INSERT INTO `userrely` VALUES ('2', '1', '0');
INSERT INTO `userrely` VALUES ('3', '1', '0');
INSERT INTO `userrely` VALUES ('4', '1', '0');
INSERT INTO `userrely` VALUES ('6', '5', '0');
INSERT INTO `userrely` VALUES ('7', '5', '0');
INSERT INTO `userrely` VALUES ('8', '5', '0');
INSERT INTO `userrely` VALUES ('9', '1', '0');
INSERT INTO `userrely` VALUES ('10', '1', '0');
INSERT INTO `userrely` VALUES ('11', '1', '0');
INSERT INTO `userrely` VALUES ('12', '1', '0');
INSERT INTO `userrely` VALUES ('13', '1', '0');

-- ----------------------------
-- Procedure structure for store_userrely
-- ----------------------------
DROP PROCEDURE IF EXISTS `store_userrely`;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `store_userrely`(suid INT,muid INT)
BEGIN
	IF
		(SELECT userinfo.ismaster FROM userinfo WHERE userinfo.uid=muid)=1
	AND
		(SELECT userinfo.ismaster FROM userinfo WHERE userinfo.uid=suid)=0
	THEN
		INSERT INTO userrely(slaveuid,masteruid) VALUES (sid,mid);
	END IF;
END
;;
DELIMITER ;
DROP TRIGGER IF EXISTS `checkmownerismaster`;
DELIMITER ;;
CREATE TRIGGER `checkmownerismaster` AFTER INSERT ON `adqm` FOR EACH ROW begin 
	IF(SELECT ismaster FROM userinfo WHERE uid=NEW.mowneruid)=0
	THEN
		DELETE FROM adqm WHERE mid=NEW.mid;
	END IF;
end
;;
DELIMITER ;
DROP TRIGGER IF EXISTS `checkexaminfoismaster`;
DELIMITER ;;
CREATE TRIGGER `checkexaminfoismaster` AFTER INSERT ON `examinfo` FOR EACH ROW begin 
	IF(SELECT ismaster FROM userinfo WHERE uid=NEW.creater)=0
	THEN
		DELETE FROM examinfo WHERE exid=NEW.exid;
	END IF;
              IF ((SELECT mowneruid FROM adqm WHERE mid=NEW.mid) != NEW.creater)
	THEN
		DELETE FROM examinfo WHERE exid=NEW.exid;
	END IF;
end
;;
DELIMITER ;
DROP TRIGGER IF EXISTS `checkginfoismaster`;
DELIMITER ;;
CREATE TRIGGER `checkginfoismaster` AFTER INSERT ON `groupinfo` FOR EACH ROW begin 
	IF(SELECT ismaster FROM userinfo WHERE uid=NEW.gowneruid)=0
	THEN
		DELETE FROM groupinfo WHERE gid=NEW.gid;
	END IF;
end
;;
DELIMITER ;
DROP TRIGGER IF EXISTS `checkganswerbool`;
DELIMITER ;;
CREATE TRIGGER `checkganswerbool` BEFORE INSERT ON `history` FOR EACH ROW begin 
	  SET NEW.answerbool = (NEW.a=NEW.selected);
end
;;
DELIMITER ;
DROP TRIGGER IF EXISTS `checkgqownerismaster`;
DELIMITER ;;
CREATE TRIGGER `checkgqownerismaster` AFTER INSERT ON `questions` FOR EACH ROW begin 
	IF(SELECT ismaster FROM userinfo WHERE uid=NEW.qowneruid)=0
	THEN
		DELETE FROM questions WHERE qid=NEW.qid;
	END IF;
end
;;
DELIMITER ;
DROP TRIGGER IF EXISTS `checkrelyismaster`;
DELIMITER ;;
CREATE TRIGGER `checkrelyismaster` AFTER INSERT ON `userrely` FOR EACH ROW begin 
	IF(SELECT ismaster FROM userinfo WHERE uid=NEW.masteruid)=0
	THEN
		DELETE FROM userrely WHERE slaveuid=NEW.slaveuid AND masteruid=NEW.slaveuid;
	END IF;
	IF(SELECT ismaster FROM userinfo WHERE uid=NEW.slaveuid)=1
	THEN
		DELETE FROM userrely WHERE slaveuid=NEW.slaveuid AND masteruid=NEW.slaveuid;
	END IF;
end
;;
DELIMITER ;
