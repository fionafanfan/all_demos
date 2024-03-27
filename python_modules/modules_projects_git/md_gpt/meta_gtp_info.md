# metagpt information

## roles - 【role-角色】

### 基本属性
   1. name-名字: 小李
   2. profile-职业: 架构师/项目经理/产品经理/开发工程师/测试工程师/销售/平台客服/教程阻力/调研人员
   3. goal-目标: xxxx
   4. constrainsts-约束条件: xxxx 
   5. desc-描述: xxxx
   6. is_human-是人类: False / True 
### 其它动作
   1. states-状态： []
   2. actions-动作: []
   3. role_id-角色属性id： {name}_{profile}
   4. rc(role-context)-角色上下文: object
   
### 角色列表
   1. 【architect-架构师】  设计一个简洁、可用、完整的python系统
   2. 【project_manager-项目经理】  负责监督项目执行和团队效率。提高团队效率，保证交付质量和数量
   3. 【product_manager-产品经理】  负责产品开发和管理的产品经理角色。有效地创造一个成功的产品
   4. 【engineer-开发工程师】  负责编写并可能审查代码。
   5. 【qa_engineer-测试工程师】  编写全面而健壮的测试，以确保代码按预期工作，没有错误
   6. 【sales-销售】  我是零售业的销售向导。我叫小梅。接下来，我将回答一些客户的问题。 只会根据知识库中的信息回答问题。
   7. 【customer_service-平台客服】  您是该平台的人工客户服务代表，将根据规则和常见问题解答进行回复。
   8. 【tutorial assistant-教程助理】  生成教程文档
   9. 【smart searcher-智能助手】  负责向用户提供搜索服务的搜索者角色。为用户提供搜索服务, 答案丰富而完整)
   10. 【researcher-调研人员】  收集信息并进行研究
   11. 【sk_agent-微软实现的语义内核】  根据传入的任务描述执行任务
   12. 【invoice ocr assistant-发票ocr助手】  发票OCR助手，支持发票PDF, png, jpg和zip文件的OCR文本识别;
生成一个包含收款人、城市、总金额和发票开具日期的表格;
并根据发票的OCR识别结果对单个文件进行提问。

## actions - 【action-动作】
