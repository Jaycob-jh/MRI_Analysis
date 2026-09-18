脑科学统计方法手册：从方法清单到 df、t、F、χ²、partial r 和 R²

面向 fMRI、dMRI、脑网络与脑刺激研究。重点是统计分析，不展开图像预处理。文献与官方方法文档核查日期：2026-09-17。下文数值例子均为教学构造，不是实际研究结果。本手册覆盖常用方法、脑影像专用推断和重要扩展，并非声称存在一张能穷尽所有统计学方法的封闭清单。

先把术语放在正确的位置：GLM、GAM、LMM 是模型；t 检验、似然比检验、置换检验是推断方法；t、F、χ² 是检验统计量；df 是用于确定参考分布或刻画模型复杂度的自由度；β、r、R²、Cohen's d 是参数或效应量；FDR 和 FWER 是多重检验的错误控制目标。一次分析通常需要同时选择这些不同层次的东西。

先给完整的方法索引。后文按同一逻辑逐类解释，重点方法包含计算公式。

| 类别 | 需要认识的方法与术语 | 脑科学中回答的问题 |
|---|---|---|
| 均值比较 | 单样本、配对、Student、Welch t 检验；单因素/多因素/Welch/重复测量/混合设计 ANOVA；ANCOVA；计划对比、简单效应、事后检验 | 组别、条件、刺激前后是否存在差异 |
| 分类与比例 | Pearson χ²、拟合优度 χ²、Fisher 精确检验、McNemar、Cochran Q、Cochran–Mantel–Haenszel | 应答率、诊断类别、配对二分类变化 |
| 秩与稳健比较 | Mann–Whitney U、Wilcoxon 符号秩、符号检验、Kruskal–Wallis、Friedman、截尾均值检验 | 偏态、异常值、有序数据的比较 |
| 相关与关联 | Pearson、Spearman、Kendall、偏相关、半偏相关、重复测量相关、稳健相关、距离相关、互信息、Fisher z 转换 | 脑指标与行为、脑区间信号的关联 |
| 线性模型 | 一般线性模型 GLM、OLS、WLS、GLS、多元线性回归、交互作用、稳健回归、分位数回归 | 控制协变量后估计效应 |
| 非高斯结局 | 广义线性模型 GLM 及扩展；logistic/probit、二项、Poisson、负二项、Gamma、Beta、有序/多项 logistic、零膨胀/障碍模型 | 二分类、计数、比例、偏态结局 |
| 重复和分层 | LMM/LME、GLMM、GEE、随机截距/随机斜率、交叉分类模型 | 重复扫描、多中心、家系、试次内相关 |
| 非线性轨迹 | 多项式、分段/变点、限制性立方样条、GAM、GAMM、GAMLSS、Gaussian process、规范模型 | 发育、衰老、剂量与时间反应曲线 |
| 估计和检验 | OLS、ML、REML、Wald、LRT、score、参数/非参数 bootstrap、置换/符号翻转、置信区间 | 参数怎样估计，不确定性怎样量化 |
| 多重比较 | FWER/FWE、FDR、Bonferroni、Holm、BH、BY、q-value、maxT、RFT、cluster、TFCE、SVC | 大量体素、脑区、连接和结局怎样控制假阳性 |
| fMRI 专用分析 | 一/二级 GLM、contrast、参数调制、FIR、seed FC、PPI/gPPI、DCM、PEB、ISC/ISFC | 任务激活、条件依赖耦合、有效连接、自然刺激同步 |
| dMRI 专用分析 | ROI/束平均分析、TBSS 统计、沿束分析、FBA、CFE、连接组边分析 | 微结构和白质通路的个体或组间差异 |
| 脑网络推断 | 边/节点/全局指标检验、NBS、TFNBS、图零模型、QAP/MRQAP、SBM、ERGM、生成模型 | 哪些连接、子网和拓扑特征不同 |
| 空间统计 | spin test、Moran 谱随机化、变差函数代理图、空间回归、空间 Gaussian process | 两张皮层图的对应是否超出空间平滑造成的相关 |
| 动态与时序 | AR/ARIMA、VAR、Granger、谱/相干性、状态空间、HMM、动态 FC | 网络状态、时滞预测、频域依赖 |
| 多变量与降维 | MANOVA/MANCOVA、Hotelling T²、PCA、ICA、因子分析、CCA、PLS、RSA、MDMR、PERMANOVA | 多个脑指标或脑—行为模式的联合关系 |
| 预测学习 | MVPA、CPM、ridge/lasso/elastic net、SVM/SVR、随机森林、梯度提升、神经网络、嵌套交叉验证、外部验证 | 能否预测新人的行为、诊断或刺激反应 |
| 机制与因果 | moderation、mediation、SEM、DAG、倾向评分、IPW、g-computation、双重稳健估计、IV、DiD、RDD | 对谁有效、通过什么路径、何种条件下可解释为因果 |
| 贝叶斯 | 层级贝叶斯、先验/后验、可信区间、Bayes factor、模型平均、后验预测检验、MCMC/VI | 参数可信范围、模型证据、个体差异 |
| 研究质量与扩展 | 功效/样本量、TOST 等效性、非劣效性、序贯分析、多重插补、敏感性分析、ICC、κ、Bland–Altman、元分析、ALE/MKDA/SDM、生存分析、心理测量/扩散决策/强化学习、圆形统计 | 研究设计、缺失、可靠性、证据整合及特定结局 |

下面先解释所有方法共用的统计语言。

1. **df：自由度怎样得到**

可以先理解为：在约束和参数估计之后，仍有多少独立信息可用于某项计算。例如 n 个残差围绕样本均值的总和为零，因此估计方差时只有 n−1 个自由度。这个直觉在普通线性模型中很有用，但混合模型和惩罚平滑中的 df 需要另行定义。

本文统一记号：n 为实际进入拟合的观测数，p 为设计矩阵 X 的秩，含截距；q 为本次同时检验的独立约束数。p 不一定等于原始变量名称个数：三水平组别通常占两列，交互作用和样条基函数也占列。

| 检验/模型 | 常见 df | 条件与解释 |
|---|---|---|
| 单样本 t | n−1 | n 个独立观测 |
| 配对 t | n−1 | n 是配对数，不是前后两次测量数之和 |
| 等方差独立样本 t | n₁+n₂−2 | 两组共享一个残差方差 |
| Welch t | Welch–Satterthwaite 近似，常为小数 | 与两组样本量和方差都有关 |
| Pearson 相关检验 | n−2 | 独立成对观测、常规参数检验 |
| 控制 c 个独立协变量的偏相关 | n−c−2 | c 不含截距，普通线性调整 |
| 普通 OLS 残差 | n−rank(X)=n−p | 独立、同方差的经典模型 |
| OLS 嵌套模型 F | df₁=q，df₂=n−p_full | q 是新增可识别参数数目 |
| k 组单因素 ANOVA | df₁=k−1，df₂=n−k | 常规等方差独立观测模型 |
| r 行 c 列独立性 χ² | (r−1)(c−1) | 没有结构零等额外约束的通常情况 |
| k 类拟合优度 χ² | 常为 k−1−a | a 为用同一数据估计的分布参数数目，需满足常规条件 |
| LMM | 依具体效应的 Satterthwaite/Kenward–Roger 等近似 | 不能机械地用扫描次数减协变量数 |
| GAM | edf、检验用 Ref.df、残差 df | 基函数受惩罚，允许小数 |
| 精确/置换检验 | 通常不靠一个参数分布 df 算 p | 仍须尊重独立性、可交换性和设计约束 |

因此，论文里的 t(95)、F(2,95)、χ²(1) 括号中通常是自由度，不是样本量。F 需要两个 df，χ² 一般需要一个。总体研究有 100 人，不表示每一项分析的 n 都是 100；缺失和筛选会改变实际样本。

2. **从数据到 β、SE、t 和 p**

一般线性模型写成：

\[
\mathbf y=\mathbf X\boldsymbol\beta+\boldsymbol\varepsilon.
\]

OLS 选择使残差平方和最小的参数。在 X 满列秩时：

\[
\widehat{\boldsymbol\beta}=(\mathbf X^\mathsf T\mathbf X)^{-1}\mathbf X^\mathsf T\mathbf y,
\qquad
\widehat{\mathbf y}=\mathbf X\widehat{\boldsymbol\beta},
\qquad
\mathbf e=\mathbf y-\widehat{\mathbf y}.
\]

\[
SSE=\sum_i e_i^2,\qquad
\widehat{\sigma}^2=\frac{SSE}{n-p},\qquad
\widehat{\operatorname{Var}}(\widehat{\boldsymbol\beta})
=\widehat{\sigma}^2(\mathbf X^\mathsf T\mathbf X)^{-1}.
\]

SE(β̂ⱼ) 就是该协方差矩阵第 j 个对角元素的平方根。实际软件通常用 QR 等稳定算法求解，不必显式求逆。

若检验 H₀:βⱼ=0：

\[
t=\frac{\widehat\beta_j}{SE(\widehat\beta_j)}.
\]

若检验某个对比 H₀:cᵀβ=δ₀：

\[
t=\frac{\mathbf c^\mathsf T\widehat{\boldsymbol\beta}-\delta_0}
{\sqrt{\mathbf c^\mathsf T\widehat{\operatorname{Var}}(\widehat{\boldsymbol\beta})\mathbf c}}.
\]

所以 t 是“估计效应离零多远，相对于它的不确定性有多大”。同样大的效应，样本更多或噪声更少，SE 较小，|t| 往往更大。t 本身不是效应量。若 β̂=0.30、SE=0.10，则 t=3；p 还需由 df 和单/双侧检验决定。

经典正态同方差模型下，双侧 p 为：

\[
p_{\text{value}}=2P(T_{n-p}\geq |t_{\text{obs}}|).
\]

95% 置信区间为：

\[
\widehat\beta_j\pm t_{0.975,n-p}SE(\widehat\beta_j).
\]

p 值是在零假设及模型假设成立时，得到当前或更极端统计量的概率；不是“零假设为真的概率”，也不是“结果由随机造成的概率”。95% 置信区间描述重复使用该构造程序的覆盖率。模型、t 对比与线性回归输出可对照 [R 的 lm 文档](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/lm.html)、[R 的 summary.lm 文档](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/summary.lm.html)及 [statsmodels 的线性对比文档](https://www.statsmodels.org/stable/generated/statsmodels.regression.linear_model.OLSResults.t_test.html)。

如果采用 GLS、异方差稳健 SE 或混合模型，β/SE 的思路仍有用，但协方差估计和参考分布可能改变。不能照搬上述经典 OLS 全套公式。

3. **F 值：一次检验一组系数**

设简化模型是“年龄+性别”，完整模型另加“组别”。两模型必须使用同一批观测，且简化模型嵌套在完整模型内。

\[
F=
\frac{(SSE_{\text{reduced}}-SSE_{\text{full}})/q}
{SSE_{\text{full}}/(n-p_{\text{full}})}.
\]

分子是新增参数平均减少多少残差，分母是完整模型剩余的每自由度噪声。F 越大，说明新增项改善拟合相对于噪声越明显。在零假设及经典模型假设成立时，其参考分布为 F(q,n−p_full)。

三组比较通常同时检验两个组别系数，所以 q=2。F 显著只说明至少有某种组间差异，不能直接告诉你哪两组不同。需要预先计划对比或有适当校正的后续比较。

若是同一个经典线性模型中、同一个单参数零假设：

\[
F_{1,\nu}=t_\nu^2.
\]

F 丢失正负方向。不同模型、不同误差估计或不同检验，不可随意套用 F=t²。尤其 GAM smooth 的 F 通常不是上述普通平方和 F。嵌套比较的样本一致性与 F 定义见 [R 的 anova.lm 文档](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/anova.lm.html)。

4. **r、partial r、semipartial r、R 和 R²**

Pearson r 是两变量的标准化线性共变：

\[
r_{xy}=
\frac{\sum_i(x_i-\bar x)(y_i-\bar y)}
{\sqrt{\sum_i(x_i-\bar x)^2\sum_i(y_i-\bar y)^2}}.
\]

r 在 −1 到 1 之间；正负表示线性关联方向，绝对值表示线性关联强度。r=0 不排除 U 形等非线性关系。

偏相关 partial r 回答：“去掉协变量能够线性解释的部分后，x 和 y 的剩余部分是否相关？”做法是分别将 x 和 y 对同一组协变量 C 回归，再计算两组残差的相关：

\[
r_{xy\cdot C}=\operatorname{cor}(e_x,e_y).
\]

只控制一个 z 时：

\[
r_{xy\cdot z}
=\frac{r_{xy}-r_{xz}r_{yz}}
{\sqrt{(1-r_{xz}^2)(1-r_{yz}^2)}}.
\]

常规线性模型下，控制 c 个独立协变量：

\[
t=r_{xy\cdot C}\sqrt{\frac{n-c-2}{1-r_{xy\cdot C}^2}},
\qquad df=n-c-2.
\]

在同一个含截距的 OLS 模型中，采用经典标准误、检验一个非截距预测变量的 H₀:βⱼ=0 时，其 t 也能转成该变量的偏相关：

\[
r_{\text{partial}}=\frac{t}{\sqrt{t^2+df}}.
\]

注意：把残差保存后直接调用普通相关检验，软件可能仍使用 n−2；若协变量来自同一数据估计，这会忘记消耗的自由度。

半偏相关 semipartial r 只从一侧去掉协变量。例如检验 x 对预测 y 的独立贡献，计算 cor(y,eₓ)。单个新增预测变量的半偏相关平方等于 ΔR²；偏相关平方通常不等于 ΔR²。

控制协变量得到的是条件关联。漏掉混杂、错误控制中介或碰撞变量，都可能改变解释；“控制了年龄和性别”本身不赋予因果意义。Pearson、秩相关及其常规检验可对照 [R 的 cor.test 文档](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/cor.test.html)。

有截距的 OLS 模型中：

\[
SST=\sum_i(y_i-\bar y)^2,\qquad
R^2=1-\frac{SSE}{SST}.
\]

R² 是当前样本中模型解释的总变异比例。例如 R²=0.40 表示相对于只预测样本均值，残差平方和减少了40%。简单线性回归只有一个预测变量且含截距时 R²=r²；多元回归的整体 R² 不能归给某一个变量。

这种情形下多重相关系数 R 可写为 cor(y,ŷ)=√R²，取非负值；它不表达某一回归效应的正负。“partial R”在不同论文中记号并不完全一致，可能指 signed partial r，也可能指一组变量的非负 partial multiple R，必须查作者定义。

| 指标 | 公式或含义 | 容易误读之处 |
|---|---|---|
| R² | 1−SSE/SST | 整个模型，不一定是组别单独的贡献 |
| 调整 R² | 1−[SSE/(n−p)]/[SST/(n−1)] | 惩罚模型复杂度，可为负 |
| ΔR² | R²_full−R²_reduced | 新增项解释的原始总变异比例 |
| partial R² | (SSE_reduced−SSE_full)/SSE_reduced | 新增项解释的“原来还没解释的变异”比例 |
| marginal R² | 混合模型中固定效应解释的变异比例 | 具体定义取决于方差分解方法 |
| conditional R² | 混合模型中固定+随机效应解释的变异比例 | 不是组别效应量 |
| pseudo-R² | logistic 等模型的若干拟合指标 | McFadden、Cox–Snell、Nagelkerke 等定义不同 |
| 样本外 R² | 独立预测误差相对于指定基准的改善 | 可以为负，需说明分母/基准 |

上述定义产生两个常用等式：

\[
R^2_{\text{partial}}
=\frac{R^2_{\text{full}}-R^2_{\text{reduced}}}
{1-R^2_{\text{reduced}}}
=\frac{qF}{qF+df_2}.
\]

单参数 q=1 时：

\[
R^2_{\text{partial}}=r_{\text{partial}}^2
=\frac{t^2}{t^2+df}.
\]

这些是指定 OLS 残差平方和定义下的等式；不要直接推广到 GAM、GLMM、正则化回归或使用稳健 SE 的任意 t/F。普通 R² 定义见 [statsmodels 的 R² 文档](https://www.statsmodels.org/stable/generated/statsmodels.regression.linear_model.OLSResults.rsquared.html)。

5. **把 df、F、t、partial r 和 R² 放进同一个算例**

假设 100 名独立受试者，完整模型为“脑指标 ~ 组别+年龄+性别+头动”，五个可识别参数含截距。简化模型删掉一个二组组别系数。假设 SST=200、SSE_reduced=100、SSE_full=80，并额外知道组别系数为正。

| 输出 | 计算 | 结果 |
|---|---|---|
| 残差 df | 100−5 | 95 |
| 完整 R² | 1−80/200 | 0.60 |
| 简化 R² | 1−100/200 | 0.50 |
| ΔR² | 0.60−0.50 | 0.10 |
| partial R² | (100−80)/100 | 0.20 |
| 组别 F | [(100−80)/1]/(80/95) | F(1,95)=23.75 |
| 组别 t | +√23.75 | t(95)=4.8734 |
| partial r | 4.8734/√(4.8734²+95) | 0.4472 |
| 调整 R² | 1−(80/95)/(200/99) | 0.5832 |
| 未校正双侧 p | 2P(T₉₅≥4.8734) | 约 4.38×10⁻⁶ |

这里“增加解释10%的总变异”和“解释20%的剩余变异”都正确，分母不同。0.4472 是有方向的偏相关，不是增加44.72%的解释率。仅有平方和不能决定 t 和偏相关的符号，所以算例额外指定了系数为正。全脑重复这样的检验后，还需另行处理多重比较。

6. **χ²：卡方检验究竟在比较什么**

最常见的独立性 χ² 检验比较分类计数的“观察值 O”与“零假设下期望值 E”：

\[
E_{ij}=\frac{(\text{第 }i\text{ 行总数})(\text{第 }j\text{ 列总数})}{N},
\qquad
\chi^2=\sum_{i,j}\frac{(O_{ij}-E_{ij})^2}{E_{ij}}.
\]

例如脑刺激试验：

| 组别 | 应答 | 未应答 | 合计 |
|---|---:|---:|---:|
| 真刺激 | 20 | 20 | 40 |
| 假刺激 | 10 | 30 | 40 |

若组别和是否应答独立，每组的期望计数都是应答15、未应答25。未经连续性校正的 Pearson χ²=5.333、df=1、p≈0.0209。这支持应答比例存在差异。效应大小还应报告应答率50%与25%、风险差25个百分点、风险比2或样本 OR=3；χ² 本身不直接给出这些临床含义。

期望计数很小或数据稀疏时，χ² 渐近近似可能不可靠，可采用 Fisher 精确或合适的 Monte Carlo 检验。前后是同一批人的二分类变化应考虑 McNemar；不能当作两批独立计数。拟合优度 χ² 则比较一个分类变量是否符合指定比例。详见 [SciPy 的列联表 χ² 文档](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.chi2_contingency.html)、[R 的 Fisher 检验](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/fisher.test.html)及 [McNemar 检验](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/mcnemar.test.html)。

另外，回归输出中的“Wald χ²”“LRT χ²”，以及 Friedman 等秩检验的 χ² 近似，都不是这张列联表上的 Pearson χ²。相同参考分布名称不等于相同计算方法。

7. **z、效应量和拟合指标也要分清**

| 名称 | 含义与计算 |
|---|---|
| Wald z | 常为 β̂/SE，使用标准正态渐近参考分布 |
| 标准化分数 z | (x−μ)/σ，表示离参考中心多少个标准差 |
| Fisher z 转换 | arctanh(r)=½log[(1+r)/(1−r)]，用于相关的变换 |
| 未标准化 β | 恒等链接线性模型中，无相关交互/非线性项时，是预测变量增加一单位对应的条件均值变化；广义模型中通常在链接尺度解释 |
| 标准化 β | 典型 OLS 定义为 β·SD(x)/SD(y)；多元模型中不等于 partial r |
| Cohen's d | 组均值差除以指定标准差；独立组与配对设计分母不同 |
| Hedges' g | 对标准化均值差作小样本偏差校正 |
| η² | 效应平方和/总平方和 |
| partial η² | 效应平方和/(效应平方和+相应误差平方和) |
| ω² | 对 η² 的偏差作一定修正的效应量 |
| Cohen's f² | (R²_full−R²_reduced)/(1−R²_full)，普通嵌套线性模型 |
| OR、RR、RD | 优势比、风险比、风险差，不能互换 |
| AIC/BIC | 拟合与复杂度的权衡指标；越小通常相对更优，没有“显著”的固定阈值 |

独立等方差两组中 d=t√(1/n₁+1/n₂)；配对设计采用差值标准差定义的 d_z=t/√n。不能把所有配对效应都称为同一种 d。

常规 ANOVA 中，使用同一效应与误差定义：

\[
\eta_p^2=\frac{Fdf_1}{Fdf_1+df_2}.
\]

虽然它的代数形式类似 partial R²，但必须确认模型和平方和定义一致。Type I 顺序平方和依变量进入顺序，Type II/III 又检验不同的调整假设；有交互项、不平衡设计时尤其应明确所检验的 contrast。

Fisher z 的常用独立二元正态近似 SE 为 1/√(n−3)，但 fMRI 时间点有自相关，不能直接把 TR 数当作 n 套用。Fisher 转换后的数不是“已经通过显著性检验的 z 分数”。

下面逐类解释模型与方法。每一类都要先确定结局类型、独立单位、研究假设，再选估计和检验。

8. **t 检验、ANOVA、ANCOVA：连续结局的基础比较**

| 方法 | 怎样做、何时使用 | 主要输出和注意点 |
|---|---|---|
| 单样本 t | 比较均值与指定值：t=(ȳ−μ₀)/(s/√n) | 例如组层任务 contrast 是否为0；df=n−1 |
| 配对 t | 先计算每人的差值 dᵢ，再做单样本 t：t=d̄/(s_d/√n) | 适合前后或两条件配对；差值分布和人之间独立性更关键 |
| Student 独立样本 t | 均值差除以合并方差得到的 SE | 等方差模型，df=n₁+n₂−2 |
| Welch t | 均值差除以 √(s₁²/n₁+s₂²/n₂) | 不要求两组方差相等；仍要求适当的独立性 |
| 单因素 ANOVA | 将总变异分为组间与组内，F=MS_between/MS_error | k 组整体均值比较，不自动定位具体组对 |
| 多因素 ANOVA | 同时估计组别、条件及交互项 | 组×条件回答组别效应是否因条件不同而改变 |
| Welch ANOVA | 对异方差多组均值比较调整权重和自由度 | 后续比较可采用匹配的 Games–Howell 等方法 |
| 重复测量 ANOVA | 分离同一人多条件中的相关结构 | 三个以上水平涉及球形性；GG/HF 可调整 df |
| 混合设计 ANOVA | 同时含组间因素与组内因素 | “混合设计”不等同于任何随机效应结构的 LMM |
| ANCOVA | 组别比较中加入连续基线或其他协变量 | 是线性模型；若组间斜率不同，需要相应交互建模 |
| 计划对比/简单效应 | 直接检验科学上指定的线性组合 | 有交互时解释在什么年龄、条件或基线下的效应 |
| Tukey/Dunnett/Games–Howell | 分别常用于所有组对、多个组对共同对照、异方差组对 | 每一种对应特定比较家族与假设 |

Welch 的自由度：

\[
\nu=
\frac{(s_1^2/n_1+s_2^2/n_2)^2}
{(s_1^2/n_1)^2/(n_1-1)+(s_2^2/n_2)^2/(n_2-1)}.
\]

例如重复测量 ANOVA 的 Greenhouse–Geisser 校正将相关的分子和分母 df 同乘 ε，使检验更符合非球形协方差；它改变参考分布，不是增加样本。不要依赖“先做正态性检验，p>.05 就保证能用参数检验”的机械流程。检查设计、残差、方差与异常值影响通常更有帮助。t 检验公式和 Welch df 见 [NIST 方法手册](https://www.itl.nist.gov/div898/handbook/eda/section3/eda353.htm)，实现区别见 [SciPy ttest_ind](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html)。

9. **秩检验、分类扩展与相关扩展**

| 方法 | 直观解释 | 主要限制或输出 |
|---|---|---|
| Mann–Whitney U / Wilcoxon 秩和 | 比较两独立组的秩分布或概率优势 | 不加共同形状等假设，不能一概说只检验中位数 |
| Wilcoxon 符号秩 | 对配对差值的绝对值排序并保留正负号 | 通常用对称差值位置模型解释；不是“完全无假设的配对 t” |
| 符号检验 | 只比较差值为正与负的数量 | 对幅度信息使用较少，可检验配对差值中位数 |
| Kruskal–Wallis | 多个独立组的秩比较 | H 在常规条件下近似 χ²(k−1)；需后续比较定位 |
| Friedman | 在同一受试者或区组内对条件排序 | 常规近似 χ²(k−1)；仍须处理重复结构 |
| Yuen/截尾均值检验 | 比较去除两端部分后估计的均值 | 目标是截尾均值，不能不说明便当普通总体均值 |
| Cochran Q | McNemar 的多个配对二分类条件扩展 | 常规近似 χ²(k−1)，不是元分析里的 Cochran Q |
| CMH 检验 | 在多个分层列联表中检验调整后的关联 | 分层如中心；共同 OR 的解释还依赖模型 |
| Spearman ρ | 对秩做 Pearson 相关 | 衡量单调关联，不是任意非线性关联 |
| Kendall τ | 比较一致与不一致的观测对 | 适合秩数据，需处理并列值 |
| 重复测量相关 | 在共同个体内线性斜率等假设下估计个体内关系 | 区别于把所有人所有时间点混在一起相关 |
| 稳健相关 | 降低异常点对关联估计的影响 | 需说明具体算法及其相应区间/检验 |
| 距离相关 | 通过样本间距离研究更一般的依赖 | 对任意维度有扩展，常用置换推断 |
| 互信息 MI | 量化知道一个变量后减少了多少另一个变量的不确定性 | 能捕捉非线性依赖；估计方法和样本偏差很重要 |

“非参数”不代表不需要独立性，不代表忽略配对设计，也不自动解决协变量调整或多重比较。秩检验的准确目标见 [R 的 Wilcoxon 文档](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/wilcox.test.html)、[Kruskal–Wallis 文档](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/kruskal.test.html)和 [Friedman 文档](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/friedman.test.html)。

10. **GLM 的两个意思，以及 OLS/WLS/GLS/稳健/分位数回归**

脑影像 GLM 经常指 general linear model，一般线性模型。模型对参数线性，不要求所有自变量都一次方。例如：

\[
y=\beta_0+\beta_1\text{Age}+\beta_2\text{Age}^2+\beta_3\text{Group}+\varepsilon
\]

仍然是一般线性模型。ANOVA、ANCOVA、多元回归和许多 fMRI contrast 都能放入这一框架。

OLS 给每个残差平方同等权重；WLS 对可靠性不同的观测赋不同权重；GLS 进一步用误差协方差表达观测之间的相关。协方差 V 已知时：

\[
\widehat\beta_{\mathrm{GLS}}
=(X^\mathsf TV^{-1}X)^{-1}X^\mathsf TV^{-1}y.
\]

实际 V 往往需要估计。fMRI 一层时序和纵向测量都可能涉及这种误差建模。

稳健回归例如 Huber M 估计，改变损失函数以降低极端残差影响；异方差稳健 SE 则可以保持 OLS 系数不变而改变不确定性估计，两者不是一回事。分位数回归拟合条件中位数或其他分位数，适合关注反应分布的不同位置，而不只关注均值。

generalized linear model，广义线性模型，则同时指定结局分布及链接函数：

\[
Y_i\sim \mathcal D(\mu_i,\ldots),\qquad g(\mu_i)=X_i\beta.
\]

高斯分布加恒等链接对应常见一般线性模型。logistic 的关系在 log-odds 尺度上线性，在概率尺度上是 S 形。因此“广义线性”并不表示结局概率随 x 走直线。广义模型常用最大似然，通过迭代加权最小二乘等数值方法求解。[R 官方广义线性模型文档](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/glm.html)

11. **广义模型各自适合什么结局**

| 模型 | 适合的结局与脑科学例子 | 效应/检查重点 |
|---|---|---|
| Logistic / Bernoulli | 应答与否、单次任务对错 | logit(p)=Xβ；exp(β) 是条件 OR，不是风险比 |
| 二项回归 | 给定试次数的成功次数 | 把分母试次数带入模型；必要时处理额外离散 |
| Probit | 二分类结局的另一种链接 | 通过标准正态分布函数连接潜在线性量与概率 |
| Poisson | 一段时间内的事件数 | log(μ)=Xβ；基础模型均值等于方差，暴露时长可用 offset |
| 负二项 | 比 Poisson 允许更大变异的计数 | 常用于过度离散；不是所有计数都必须用它 |
| Gamma / 对数正态模型 | 正值且偏态的反应时等 | 二者分布假设不同，均值解释需注意链接/变换 |
| Beta 回归 | 严格在0和1之间的连续比例 | 原始0/1边界需额外模型；不等同于成功次数/总次数的二项模型 |
| 有序 logistic/probit | 有序症状等级 | 比例优势等约束需要检查 |
| 多项 logistic | 无序多类别诊断/状态 | 输出相对参考类别的效应 |
| 零膨胀模型 | 计数中可能存在额外结构零 | 混合“额外零”过程与通常计数过程 |
| Hurdle 障碍模型 | 是否为零及大于零后的数值由不同机制描述 | 两部分分别建模，正值部分被截断 |

这些模型常报告 β、SE、Wald z/χ²、LRT、deviance 和相应效应比例，不一定报告普通 R²。需要区分均值模型、离散参数以及观测相关结构；重复二分类数据还需要 GLMM/GEE 等。

12. **LMM、GLMM、GEE：同一个人多次测量怎样处理**

LMM 又常称 LME 或线性混合效应模型。例如脑刺激前后：

\[
y_{it}=
\beta_0+\beta_GG_i+\beta_TT_t+\beta_{GT}G_iT_t
+b_{0i}+\varepsilon_{it}.
\]

固定效应 β 描述总体平均关系；随机截距 b₀ᵢ 描述每个人的起点偏差，通常设随机效应来自均值为0的分布。同一人的多条记录共享这个偏差，所以彼此相关。有足够重复测量或合适约束时，还可加入 b₁ᵢTₜ，让每个人有不同变化斜率；每人仅两次观测时，不能不加约束就自由估计随机截距/斜率的完整协方差及残差方差。

两时间点、0/1 编码下，β_GT 就是两组前后变化之差。100 人各3次扫描，不等于300个独立受试者。中心、家系、受试者和刺激材料也可形成嵌套或交叉分类结构，但随机效应复杂度需要数据支持。

LMM 中 t=β̂/SE 仍常出现，但分母 df 一般不能直接用 n−p。Satterthwaite 估计近似 df；Kenward–Roger 还会修正相关协方差或 F 统计量，因此可能得到小数 df。随机效应方差等需单独解释。见 [lmerTest 原始论文](https://www.jstatsoft.org/article/view/v082i13)与 [lme4 的 p 值说明](https://lme4.github.io/lme4/reference/pvalues.html)。

GLMM 把结局换成二项、计数等，并对给定随机效应的条件均值使用链接函数，常报告 Wald z、LRT 和随机效应方差。

GEE 不必完整指定个体随机效应分布，而是对人群平均关系建模，使用工作相关结构及 sandwich SE。其稳健性需要正确的均值模型、足够独立聚类和其他常规条件；少量受试者不能靠“稳健”两个字自动解决。非线性链接下，GLMM 的个体条件效应和 GEE 的总体平均效应通常不同。GEE 一般不是完整似然模型，因此普通 LRT/AIC 不能直接照搬。[Liang 与 Zeger 的 GEE 原论文](https://www.maths.usyd.edu.au/u/jchan/GLM/Liang%26Zeger1986GEE.pdf)

13. **GAM：怎样估计一条非线性曲线，edf 又是什么**

GAM 是 generalized additive model，广义加性模型：

\[
g\{E(Y_i)\}=\beta_0+f_1(\text{Age}_i)+f_2(\text{Dose}_i)+\beta_GG_i.
\]

它适合年龄与皮层厚度、FA、网络效率的弯曲关系，也适合刺激剂量反应。加性指各项相加；需要年龄×剂量等非线性交互时可加入二维/张量积平滑，GAM 并非完全不能有交互。[mgcv的模型设定说明](https://stat.ethz.ch/R-manual/R-devel/library/mgcv/html/gam.models.html)

软件先把曲线写成基函数组合：

\[
f(x)=\sum_{k=1}^K b_k(x)\theta_k.
\]

高斯模型下，以“拟合误差+弯曲惩罚”估计系数：

\[
\min_{\theta}
\left[
\sum_i(y_i-\widehat y_i)^2+
\lambda\theta^\mathsf TS\theta
\right].
\]

λ 越大通常曲线越平滑；λ 由 REML、GCV 等准则估计或选择。[mgcv的GAM估计文档](https://stat.ethz.ch/R-manual/R-devel/library/mgcv/html/gam.html) K 是基函数维度上限，不等于最终自由度，更不等于拐点数。[mgcv基函数维度说明](https://stat.ethz.ch/R-manual/R-devel/library/mgcv/html/choose.k.html)

给定平滑参数的线性平滑器可写为 ŷ=Ay。模型有效自由度：

\[
edf_{\mathrm{model}}=\operatorname{tr}(A).
\]

在上述线性平滑器及常用软件近似下，残差自由度可写为 df_res≈n−tr(A)，不是n−基函数数量。它与近似检验使用的Ref.df仍须区分。

每个平滑项有自己的 edf 贡献。对常见保留线性部分的一维平滑，edf≈1 表示链接尺度上近似直线；edf 较大表示可表达更复杂的形状；收缩平滑还可能将项压到更小的 edf。

| GAM 输出 | 应怎样读 |
|---|---|
| Parametric coefficients | 普通线性项的 β、SE、t/z、p |
| edf | 平滑项的有效复杂度 |
| Ref.df | 近似显著性检验用的参考自由度，未必等于 edf |
| F 或 χ² | 对整个平滑项的近似检验统计量 |
| p-value | 通常检验 H₀:f(x)≡0 |
| R-sq.(adj) / Deviance explained | 整体模型拟合指标，不是某个 smooth 的 F |

平滑检验综合平滑系数及其协方差，可从 Wald 型二次形式理解，然后根据尺度与有效秩给出近似 F/χ²。不能把 smooth 的 edf 当作普通新增参数数目，照抄前面的 OLS 平方和 F。

mgcv默认平滑p值以估计出的平滑参数为条件，没有计入其估计不确定性；这类不确定性较大时，p值可能偏小。因此应结合曲线、区间、模型诊断与敏感性分析解释。

若虚构输出为 edf=4.6、Ref.df=5.7、F=8.2、p<.001，可说“控制其他项后，年龄曲线整体与脑指标有关，拟合形状有一定复杂度”。不能说“4.6个拐点”“年龄解释8.2%方差”“每个年龄点都显著”。

尤其是：**平滑项显著，不等于非线性部分显著。**显著直线也能让整个 smooth 显著。研究问题若是“是否弯曲”，需明确检验超出线性部分的成分；若问“在哪些年龄增加”，需要导数 f′(age) 和相应区间；多年龄点结论需区分点态与同时置信带。[mgcv 的 summary.gam](https://stat.ethz.ch/R-manual/R-devel/library/mgcv/html/summary.gam.html)、[Wood 2013 平滑项检验原论文](https://academic.oup.com/biomet/article/100/1/221/192816)、[mgcv 的模型比较限制](https://stat.ethz.ch/R-manual/R-devel/library/mgcv/html/anova.gam.html)

14. **GAMM、GAMLSS、样条、Gaussian process 和规范模型**

GAMM 是 GAM 加混合效应，例如：

\[
y_{it}=\beta_0+f(\text{Age}_{it})+\beta_GG_i+b_{0i}+\varepsilon_{it}.
\]

它同时表达非线性总体轨迹和重复扫描的相关性。还可建立随机斜率、分组曲线、个体曲线，但“每组曲线分别显著”并不是两组曲线有差异，需要直接检验差异函数或模型中的相应项。GAMM 是模型类别，不等于某一个软件函数；不同实现使用的似然或近似方法可能不同。[mgcv 的 gamm 文档](https://stat.ethz.ch/R-manual/R-devel/library/mgcv/html/gamm.html)

GAMLSS 允许条件分布的位置、尺度和形状分别随年龄等变化：

\[
Y_i\sim D(\mu_i,\sigma_i,\nu_i,\tau_i),\qquad
g_\mu(\mu_i)=f_\mu(a_i),\quad
g_\sigma(\sigma_i)=f_\sigma(a_i).
\]

这样不仅平均脑体积随年龄变化，个体间分散程度和分布偏斜也可以变化；μ、σ 在具体分布参数化中不必恰好等于均值和标准差。[GAMLSS 原始软件论文](https://www.jstatsoft.org/article/view/v023i07)

其他非线性方法也有各自目标：

| 方法 | 如何表达非线性 | 使用边界 |
|---|---|---|
| 多项式回归 | 加 Age²、Age³ 等 | 易于检验系数，但高阶多项式边界可能不稳定 |
| 限制性立方样条 | 在结点间用平滑多项式，限制边界行为 | 结点与自由度需说明；可联合检验非线性基函数 |
| 分段/变点模型 | 允许某个年龄或剂量前后斜率改变 | 若变点由数据选择，其不确定性应计入推断 |
| Gaussian process | 用均值函数和协方差核为函数定义概率分布 | 提供非线性预测与不确定性，依赖核及噪声模型 |
| 函数型数据分析 | 把整条沿束/时间曲线当作一个函数对象 | 函数回归、函数主成分、同时置信带处理曲线结构 |
| 规范模型 | 学习参考人群的条件分布，再定位个人偏离 | 可以用 GAMLSS、GP、层级回归等，不是单一算法 |

规范模型问的是“这个人的脑指标相对于同年龄等参考条件处在什么位置”，不是仅检验患者平均值是否不同。常输出百分位、标准化偏离和预测区间；需样本外校准与适当参考样本。脑生命周期图谱是 GAMLSS 的代表性脑影像应用。[Bethlehem 等，Brain charts for the human lifespan](https://www.nature.com/articles/s41586-022-04554-y)

15. **ML、REML、Wald、LRT、score、AIC/BIC：估计模型与比较模型**

ML 最大似然估计选择使已观测数据最可能的参数；REML 在估计方差成分时考虑固定效应估计造成的信息消耗，常用于 LMM，也用于 GAM 的平滑参数估计。它们是估计原则，不是一种结局变量，也不自动决定显著性。

Wald 检验看“参数估计离零有多远”，单参数常是 β̂/SE 或其平方；多参数使用系数向量与协方差构成二次型。LRT 似然比检验比较嵌套模型：

\[
LR=2\{\ell_{\text{full}}-\ell_{\text{reduced}}\}.
\]

在通常可识别、参数位于内部等正则条件及大样本下，LR 近似服从 χ²(q)，q 是独立参数数目差。score 检验只需在零假设模型处计算似然的一阶导数及信息量，问“沿备择方向移动是否值得”。三种检验大样本时可能接近，小样本时不必一样。

随机效应方差为0处在参数空间边界，因此检验“有没有随机效应”时，普通 χ²(q) 近似不总成立。比较固定效应不同的 LMM，不能直接比较各自 REML 似然，通常应改用 ML；再选择适合的 Wald、LRT 或参数 bootstrap。[lme4 官方模型比较说明](https://lme4.github.io/lme4/reference/merMod-class.html)

信息准则常写成：

\[
AIC=-2\widehat\ell+2k,\qquad BIC=-2\widehat\ell+k\log n.
\]

k 是似然模型中的估计参数数目，包含哪些方差等参数须按模型定义。AIC/BIC 用于同一数据及可比似然下的相对比较；不是零假设检验，也不能代替样本外验证。GAM 等的有效复杂度处理需按实现解释。

16. **Bootstrap 和置换：看起来都在“重抽”，目标不同**

Bootstrap 从经验样本或拟合模型反复生成新样本，近似估计量的抽样不确定性，可构造 SE、置信区间及稳定性结果。非参数 bootstrap 常有放回地抽受试者；参数 bootstrap 则从拟合的概率模型生成数据。重复扫描应按人/聚类抽取，时间序列可需块 bootstrap；不能把本来相关的观测当独立抽样单位。

置换检验按零假设允许的方式重排组别、记录或残差，产生“无目标效应时”的统计量分布。配对分析可能使用符号翻转；家系和重复测量需受限交换；含协变量的 GLM 可能使用 Freedman–Lane 等残差方案。置换不是任意乱序，也不是没有模型假设。

若随机生成 B 个零分布统计量，常用 Monte Carlo p：

\[
\widehat p=\frac{1+\#\{T_b^\ast\geq T_{\mathrm{obs}}\}}{B+1}.
\]

例如9999次随机重排，常用形式的最小可报告 p 是0.0001，而不是0。穷举全部允许排列时使用相应精确计数。符号翻转、双侧统计量、交换块和协变量处理应服从实际设计。[Winkler 等2014，GLM置换推断原论文](https://pubmed.ncbi.nlm.nih.gov/24530839/)、[FSL randomise 官方说明](https://fsl.fmrib.ox.ac.uk/fsl/docs/statistics/randomise.html)

17. **FWE/FWER 与 FDR：究竟控制哪种错误**

定义一组同时检验的假设为一个 family。设 V 是错误拒绝的数量，R 是总拒绝数量：

\[
FWER=P(V\geq1),\qquad
FDR=E\left[\frac{V}{\max(R,1)}\right].
\]

FWE correction 通常指控制 FWER：在整个 family 中至少出现一次假阳性的概率不超过 α。FDR 则控制宣布显著者中假阳性比例的期望。两者不是统计模型，也不是效应量。

例如全部零假设都真的情况下，做100次相互独立且每次α=.05的检验，至少一个假阳性的概率为 1−0.95¹⁰⁰≈99.4%。脑数据未必独立，但这说明单次α不能直接当作整组α。

FDR控制在.05不意味着“每条显著边有5%概率是假的”，也不保证当前数据中假发现比例必然≤5%。如果全部零假设都为真，任何发现都是假的，此时 FDR=FWER。

| 校正方法 | 操作 | 控制目标与条件 |
|---|---|---|
| Bonferroni | p_adj=min(mp,1)，或阈值α/m | FWER；不要求检验之间独立 |
| Holm | 对排序p依次用α/(m−i+1)，首次不通过后停止 | FWER；任意依赖下有效，通常比单纯Bonferroni更有力 |
| Šidák | 单次阈值1−(1−α)^(1/m) | 独立检验时的家族控制，不能无条件套到相关脑区 |
| Hochberg/Hommel | 基于排序p的进一步家族控制程序 | 需相应独立性或依赖条件，不能与Holm无条件互换 |
| BH | 找最大k满足p_(k)≤(k/m)q，拒绝前k个 | FDR；经典保证依赖独立或规定的正依赖条件 |
| BY | BH中的q除以∑(1/j) | 任意依赖下的FDR保证，常较保守 |
| Storey q-value | 估计真零比例并评估包含该发现的拒绝区域的FDR/pFDR | 不必等于BH调整p，也不等于单个假设的后验错误概率 |
| maxT / maxF | 每次置换保存整个家族最大统计量 | 用最大值零分布做位置层面的家族校正 |

五个原始 p 为 .001、.012、.021、.040、.200。BH 的 q=.05 阈值依次为 .01、.02、.03、.04、.05，前四项通过；Bonferroni 阈值为 .01，只有第一项通过。BH 调整 p 依次为 .005、.030、.035、.050、.200。BH 是找最大通过的排序位置，不能误写成像 Holm 一样“遇到一次不通过就停止”。

FWER/FDR 的算法与条件见 [R p.adjust 文档](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/p.adjust.html)、[BH原论文](https://doi.org/10.1111/j.2517-6161.1995.tb02031.x)、[BY原论文](https://doi.org/10.1214/aos/1013699998)和 [Storey的q-value相关原论文](https://genomics.princeton.edu/storeylab/papers/directfdr.pdf)。

local FDR 指给定局部统计证据时零假设的模型化后验概率，与整组发现上的 FDR/q-value 不同。FDR 校正一般不重新产生一个 df：每条边先由其模型得到统计量、df和原始p，再校正整组p。上游把重复测量当独立样本造成的错误，BH不能修复。

18. **全脑空间推断：voxel/vertex、cluster、RFT、TFCE、SVC**

| 方法/层级 | 在做什么 | 显著性可以支持什么 |
|---|---|---|
| Voxel/vertex-wise | 对每体素/表面顶点拟合模型并进行多重控制 | 在所采用位置推断框架下定位效应 |
| Peak-wise | 检验局部峰高度 | 需要相应峰/随机场推断，不能把输出所有栏位都叫同一种p |
| Cluster extent | 先过成簇阈值，再检验连续簇的大小 | 显著性属于簇整体 |
| Cluster mass | 检验簇内统计量的累计强度 | 同样需要适当簇零分布 |
| RFT 随机场理论 | 用统计场平滑度和几何近似峰/簇概率 | resels 描述有效空间分辨单元，不是被试df |
| TFCE | 综合多个高度阈值下的高度与邻域支持 | 需要进一步用最大TFCE等零分布校正 |
| SVC 小体积校正 | 在预先或独立定义的搜索区域内控制错误 | 不能看本数据结果后随意缩小区域来降低校正负担 |

TFCE 的概念式为：

\[
TFCE(v)=\int_0^{h(v)} e_v(u)^E u^H\,du.
\]

eᵥ(u) 是阈值u下包含位置v的簇大小。此式针对非负统计量或正向分支；双侧t需按实现处理正负方向，并控制两个方向合并后的错误率。TFCE 不需要选择一个单一成簇阈值，但仍有E、H等参数，而且TFCE变换本身还不等于FWE校正。[Smith与Nichols的TFCE原论文](https://pubmed.ncbi.nlm.nih.gov/18501637/)

簇显著不能证明簇内每一个体素都单独显著，更不能把边界当成精确生物学边界。参数簇推断依赖空间模型假设；其失配可能影响假阳性率。[Eklund等2016原研究](https://www.pnas.org/doi/10.1073/pnas.1602413113)。

研究应明确 family 包括哪些体素/脑区/边、哪些方向和contrasts，以及多个结局或频段怎样处理。只报告“p<.05, corrected”不够判断结果。

19. **任务 fMRI：一层 GLM、二层 GLM、contrast 与参数调制**

一层模型通常对每位受试者、每个位置的时间序列拟合：

\[
y_v(t)=\sum_k X_k(t)\beta_{vk}+\varepsilon_v(t).
\]

设计矩阵中的任务回归量可由事件序列与HRF卷积构建。β衡量对应回归量的贡献，contrast 是它们的线性组合；例如β_A−β_B检验条件A与B之差。若用多个HRF基函数或FIR时间箱表达形状，可用F联合检验一组参数。

参数调制将试次强度、难度、价值等连续变量带进模型，问BOLD反应是否随该变量变化。存在相关调制量时，要说明顺序、中心化及是否正交化，因为这些会改变系数的条件含义。

二层分析将每人的contrast或其他摘要作为观测，使用组层t、GLM、LMM等推断人群效应。二层df通常围绕受试者数量和组层设计；一层df围绕时间序列、设计及误差相关结构。把所有人的TR直接拼接后视作独立观测不能代替适当的人群随机效应推断。

FFX固定效应合并与RFX/混合效应人群推断的推广目标也不同。多个session、不同个体估计精度和异方差应由相应层级模型处理。这里提及HRF与误差相关是为解释统计模型，不展开预处理。[SPM任务GLM与contrast官方教程](https://www.fil.ion.ucl.ac.uk/spm/docs/tutorials/fmri/modelling/block_design/)

20. **功能连接、偏相关网络、PPI/gPPI、DCM/PEB、ISC/ISFC**

| 方法 | 研究问题和计算对象 | 输出与推断单位 |
|---|---|---|
| Seed-based FC | 一个种子脑区与全脑其他位置共同变化程度 | 每人一张r/Fisher-z图，再进行组层模型 |
| ROI-to-ROI FC | 多个脑区时间序列的成对关联 | 每人一张连接矩阵；边级/子网级推断 |
| 精度矩阵/高斯图模型 | 控制已纳入的其他变量后，是否仍有条件关联 | 逆协方差与偏相关；高斯条件下零元素对应条件独立 |
| Graphical lasso | 高维、有限样本中估计稀疏精度矩阵 | 正则化边和稳定性；非零边不直接等于显著边 |
| PPI | 种子与目标耦合是否随任务情境变化 | 任务×种子信号交互系数、t或contrast |
| gPPI | 多个任务条件各自的耦合变化及差异 | 各条件交互及联合/差异对比 |
| DCM | 指定的神经动态及测量模型怎样解释数据 | 有效连接参数后验、模型证据 |
| PEB | DCM连接参数在组层怎样随年龄/治疗等变化 | 传播个体参数不确定性的层级贝叶斯推断 |
| ISC | 自然刺激下，不同人同一区域的反应是否同步 | 被试间时间序列相关及依赖结构下的组推断 |
| ISFC | 不同人不同区域的反应是否共同变化 | 跨被试连接；需相应配对依赖处理 |

若Θ=Σ⁻¹，偏相关网络为：

\[
r_{ij\cdot\text{others}}=-\frac{\Theta_{ij}}{\sqrt{\Theta_{ii}\Theta_{jj}}}.
\]

它只控制模型中实际纳入的其他变量，不能排除未知共同输入。正则化产生的网络不再直接适用普通无惩罚偏相关t检验。[Smith等的fMRI网络方法研究入口](https://www.fmrib.ox.ac.uk/datasets/netsim/)

PPI可以用简化交互模型理解：

\[
Y=\beta_0+\beta_PP+\beta_SS+\beta_{PS}(P\times S)+C\gamma+\varepsilon.
\]

关键是β_PS。PPI不是单纯“激活增加”，也不单独证明方向性因果。gPPI将多个任务条件的交互同时建模；实际实现还考虑神经信号与血流动力学关系。[McLaren等2012 gPPI原论文](https://pubmed.ncbi.nlm.nih.gov/22484411/)

DCM使用明确的神经动力学和观测模型；其“causal”解释依赖模型、实验与可识别性。PEB将个体连接参数的后验不确定性纳入组层分析。常见输出是后验均值、区间和模型证据，不需要强行为每项配一个普通t(df)。[Zeidman等的DCM/PEB群体分析教程](https://arxiv.org/abs/1902.10604)

ISC中n个人可产生n(n−1)/2个两两相关，但这些相关共享受试者，并不独立。应使用针对两端被试的混合效应或适当被试重采样。[AFNI 3dISC官方文档](https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dISC.html)

21. **dMRI：ROI、TBSS、沿束和 FBA 的统计层**

| 分析 | 统计上在比较什么 | 常见模型与注意点 |
|---|---|---|
| ROI/纤维束平均 | 每人每个ROI或束的FA、MD等 | GLM/LMM/GAMM；多个ROI仍需定义检验家族 |
| TBSS统计 | 白质骨架上每位置的指标 | GLM、contrast、置换、TFCE/FWE |
| 沿束统计 | 同一纤维束不同位置的指标曲线 | 点位模型+校正，或函数型模型/平滑混合模型 |
| FBA | 同体素内不同纤维群fixel的指标 | FD、FC、FDC的组模型与CFE/置换 |
| 结构连接组 | 每人连接矩阵中的边、子网或图指标 | 边级模型、NBS、预测或图生成模型 |

TBSS、FBA是分析框架，不是与t检验互斥的另一种“单一统计检验”。最终t/F来自设计矩阵与误差模型。FBA中FD为fibre density，FC为fibre cross-section，FDC为二者乘积；这里FC不是functional connectivity。CFE利用fixel之间的连接信息增强推断。参考 [FSL TBSS文档](https://fsl.fmrib.ox.ac.uk/fsl/docs/diffusion/tbss.html)和 [MRtrix FBA文档](https://mrtrix.readthedocs.io/en/latest/fixel_based_analysis/mt_fibre_density_cross-section.html)。

FA或纤维指标差异显著并不对应唯一组织学机制；统计推断与生物物理解释需要分别论证。DTI/NODDI等模型参数的测量原理属于另一层，这里关注这些参数得到之后怎样比较。

22. **脑网络：图指标、NBS、TFNBS、网络零模型、SBM/ERGM**

| 网络量/方法 | 含义 | 统计解释 |
|---|---|---|
| Degree / strength | 节点连接条数/连接权重之和 | 描述节点连接规模 |
| Clustering | 邻居之间相互连接程度 | 描述局部组织 |
| Path length / efficiency | 最短路径长度/其倒数的汇总 | 描述图论可达性；权重到距离的映射须明确 |
| Modularity Q | 给定零模型下的模块内连接集中程度 | 模块划分与分辨率参数会影响Q |
| Participation coefficient | 节点连接分布在不同模块的程度 | 依赖采用的模块划分 |
| Centrality / rich club | 节点位置重要性/高连接节点的互联结构 | 要明确具体定义和匹配零模型 |
| NBS | 检验一组拓扑相连的异常边 | 显著性通常属于连通分量 |
| TFNBS | 跨多个阈值积累图邻域支持 | 对边的增强统计量做置换校正 |
| QAP/MRQAP | 同步置换矩阵行列，检验矩阵对应/回归 | 处理节点标记对应的依赖，不自动解决空间混杂 |
| SBM | 以节点分块解释边生成概率 | 输出块结构和概率参数，不保证每块都是高密度社团 |
| ERGM | 用边数、三角形等网络统计量定义整张图的概率模型 | 表达边依赖，需检查退化、拟合和可识别性 |
| 图生成模型 | 用距离、拓扑偏好等规则解释连边 | 比较参数与模拟网络；拟合好不等于证明发育机制 |

算出某人的全局效率后，还要通过跨被试t/GLM/LMM等做组间推断。单个人几千条边不能当作几千个独立被试。网络密度、权重、负边处理、阈值与模块分辨率都可能影响指标，须结合研究目标检验敏感性。[Rubinov与Sporns的网络指标方法论文](https://pubmed.ncbi.nlm.nih.gov/19819337/)

NBS通常先对每条边算t/F，设定初始阈值，将超阈边组成连通分量，再把观测分量的边数（extent）或边级检验统计量之和（intensity）与置换中的最大分量比较。intensity不是原始FC或纤维数权重之和。原方法的FWE保证与分量/全零假设有关，不能表述为对所有单边零假设的任意组合都提供强FWER控制。**一个NBS显著子网不代表其中每条边都独立通过FWE校正。**初始阈值会改变被检出的网络结构。[Zalesky等2010 NBS原论文](https://pubmed.ncbi.nlm.nih.gov/20600983/)

TFNBS将TFCE思路移到图上，对每条边得到受邻域支持的增强统计量，再以全连接组最大增强值的置换分布计算边级校正p。它与NBS的分量p不同，仍需指定增强参数。[Baggio等2018 TFNBS原论文](https://onlinelibrary.wiley.com/doi/full/10.1002/hbm.24007)

随机重连可以保留度、强度或距离结构，问“观察拓扑是否超出这些约束”。这与重排被试组别、问“患者和对照是否不同”是两种零假设。跨网络密度的指标曲线AUC也不是分类的ROC-AUC。

QAP/MRQAP的节点重标记与回归见 [QAP文档](https://rdrr.io/cran/sna/man/qaptest.html)；概率图生成与分块建模见 [SBM官方教程](https://graph-tool.skewed.de/static/docs/stable/demos/inference/inference.html)和 [ERGM官方教程](https://statnet.org/workshop-ergm/ergm_tutorial.html)。

23. **空间对应：spin、Moran、BrainSMASH**

如果两张皮层图都很平滑，相邻脑区不是独立样本。直接把200个脑区放入普通相关、用df=198算p，可能低估不确定性。

Spin将球面皮层图旋转以改变空间对应；Moran谱随机化通过空间权重矩阵的特征结构生成替代图；BrainSMASH通过匹配距离与图差异的变差函数生成空间代理图。它们通常保持观测r不变，改变用于评价r是否异常的零分布。

Spin主要适合可球面化的皮层；内侧壁、映射和球面失真需考虑，不能简单套到皮层下。Moran和变差函数方法也需要核查代理图是否保留目标空间结构。[Alexander-Bloch等2018 spin原论文](https://pubmed.ncbi.nlm.nih.gov/29860082/)、[BrainSpace空间零模型教程](https://brainspace.readthedocs.io/en/latest/python_doc/auto_examples/plot_tutorial3.html)、[BrainSMASH方法说明](https://brainsmash.readthedocs.io/en/latest/approach.html)

空间零模型不自动进行多重比较校正。比较许多受体图、基因图或功能图时，仍需处理多重检验。群体平均图上的空间关联也不等同于个体层面的脑—行为关系。

24. **动态与时序：AR、VAR、Granger、HMM、状态空间、谱/相干性**

| 方法 | 核心建模对象 | 常见输出和边界 |
|---|---|---|
| AR/ARIMA | 变量自身过去对现在的预测，及趋势/差分/移动平均结构 | 时序系数、预测区间、残差诊断 |
| VAR/MVAR | 多个脑区过去共同预测当前活动 | 滞后系数矩阵、残差协方差、阶数 |
| Granger | 加入X过去后，是否改善Y的预测 | 受限/完整模型的F或似然比较；不自动证明生物因果 |
| 状态空间模型 | 潜在状态随时间演变，并产生有噪声观测 | 潜在状态估计及不确定性；Kalman滤波是其计算工具之一 |
| HMM | 数据在离散潜在状态间切换 | 状态概率、均值/协方差、转移、占有率、停留时间 |
| Sliding-window FC | 在连续时间窗口估计连接 | 窗宽敏感；噪声能产生波动，不等于已证明非平稳 |
| 谱/相干性 | 频域能量及两信号在各频率的关联 | 频率分辨率、平滑和分段影响估计和自由度 |

VAR可写成：

\[
x_t=c+\sum_{\ell=1}^{L}A_\ell x_{t-\ell}+\varepsilon_t.
\]

Granger检验通过删除某来源变量的一组滞后系数，形成嵌套模型比较；df需考虑可用时间点和滞后参数。fMRI的血流动力学延迟与采样速度影响时滞方向解释。动态FC/HMM产生每人的状态摘要后，组间差异仍可用GLM/LMM/GAMM检验，df来自这个后续模型。[Vidaurre等2017 HMM脑动态原研究](https://www.pnas.org/doi/10.1073/pnas.1705120114)

25. **多变量分析：MANOVA、PCA、ICA、CCA、PLS、RSA、MDMR**

| 方法 | 在优化或检验什么 | 如何读输出 |
|---|---|---|
| MANOVA/MANCOVA | 联合检验多个结局的组间差异，后者调整协变量 | Wilks' Λ、Pillai trace等；可能转换成近似F |
| Hotelling T² | 将均值差向量按协方差标准化 | 多变量t类检验，需可估计的协方差 |
| PCA | 寻找解释X方差最多的正交方向 | λⱼ/∑λ是该成分解释方差比例，不是行为预测R² |
| 因子分析 | 用潜变量解释多个观测指标的共同变异与测量误差 | 载荷、独特方差、潜变量；与PCA目标不同 |
| ICA/group ICA | 寻找统计上尽可能独立的成分 | 空间图、时间序列、阶数；空间ICA不要求时间序列互不相关 |
| Dual regression | 从群体成分获得个体时间序列与空间表达 | 个体图再进入组层模型和校正 |
| CCA | 找u=Xa、v=Yb，使cor(u,v)最大 | canonical r、权重、载荷、留出集关联 |
| 关联型PLS | 找两组投影共同变化最大的方向 | 潜变量、奇异值、协方差解释、置换/稳定性 |
| PLS regression | 用与Y有关的X潜变量预测Y | 成分数、系数、交叉验证误差 |
| RSA | 比较脑、行为或模型的表征差异矩阵RDM | RDM相似性、距离；共享刺激的条目不独立 |
| MDMR/PERMANOVA | 检验被试间距离结构与组别/协变量的关系 | pseudo-F、R²、置换p；不是自动采用经典F分布 |

CCA、PLS通常需要置换检验总体模式和bootstrap评估权重稳定性；bootstrap ratio不能不加定义地当作普通t。高维小样本中的样本内canonical r容易乐观，稳定性和样本外验证非常重要。[Helmer等2024 CCA/PLS稳定性原研究](https://www.nature.com/articles/s42003-024-05869-4)

ICA提供成分模型，不自动证明某个成分是一个独立生物模块。[Beckmann与Smith概率ICA论文](https://pubmed.ncbi.nlm.nih.gov/14964560/)；RSA的统计单位需尊重受试者和刺激的抽样结构。[Kriegeskorte等RSA原论文](https://www.frontiersin.org/journals/systems-neuroscience/articles/10.3389/neuro.06.004.2008/full)

PERMANOVA显著既可能反映组中心位置，也可能受组内离散程度影响，不能直接写成“多变量均值有差异”。[vegan adonis2官方文档](https://vegandevs.github.io/vegan/reference/adonis.html)

26. **预测：MVPA、CPM、正则化、机器学习与验证**

MVPA是利用多个体素/特征进行模式分析的范式；searchlight是遍历局部空间窗口的策略，不是单一分类器。CPM通常在训练集中筛选与行为关联的边，汇总成网络强度，再预测留出受试者。筛边的p值是模型选择步骤，不是最终预测显著性。[Shen等CPM方法论文](https://pubmed.ncbi.nlm.nih.gov/28182017/)

Ridge对系数平方和惩罚，使相关特征的权重收缩；lasso使用绝对值惩罚，可使部分系数为零；elastic net结合两者。SVM/SVR用间隔/容差及核函数建分类或回归模型；随机森林集成多棵树；梯度提升逐步拟合损失；神经网络学习多层非线性表示。模型复杂度提高不保证样本外性能提高，选出的特征也不自动具有因果或显著性含义。

连续预测常报告MAE、RMSE、预测相关r、样本外R²；分类报告accuracy、balanced accuracy、灵敏度、特异度、ROC-AUC，类别不平衡时还可看PR-AUC，并检查概率校准。

\[
R^2_{\mathrm{test}}
=1-\frac{\sum_{i\in test}(y_i-\widehat y_i)^2}
{\sum_{i\in test}(y_i-\overline y_{\mathrm{test}})^2}.
\]

这里展示的是常见测试集均值基准，其他预先指定基准也存在，报告时应说明。它可以为负，表示比基准更差。预测相关r只反映同步程度，不能检查偏移和尺度。若y=(1,2,3)，ŷ=(101,102,103)，r=1但R²=−14999，因此预测r²不等于预测R²。[scikit-learn R²官方定义](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html)

验证应匹配推广目标：预测新人按人划分，家系按家系划分，检验新中心推广时需中心外验证。特征选择、标准化参数、PCA、协变量处理与调参都应限制在相应训练数据内；调参用内层、评估用外层。计算置换p时，应按设计重跑包含选择与调参的流程。各折共享训练信息，不是独立实验，不能把折分数直接当独立样本随便做t检验。[Varoquaux等脑解码验证原研究](https://arxiv.org/abs/1606.05201)

27. **脑刺激试验：基线调整、组×时间、交叉设计与剂量**

随机平行组、一个基线一个主要终点时，常用基线调整ANCOVA：

\[
Y_{\mathrm{post}}=\beta_0+\tau G+\gamma Y_{\mathrm{pre}}+C\beta+\varepsilon.
\]

τ是给定基线和协变量的终点组差；其估计与t/CI来自这个模型。预先定义基线调整，不宜按“基线是否显著不同”临时决定是否调整。随机试验中的这些解释不能无条件移植到非随机分组。[Vickers与Altman基线/随访分析论文](https://pubmed.ncbi.nlm.nih.gov/11701584/)

多次随访可用LMM/MMRM，时间可以是分类变量或曲线。两时间点、组别与时间均用0/1编码时，组×时间系数是两组变化之差。**真刺激组前后p<.05、假刺激组p>.05，不等于刺激效果显著优于假刺激**；必须直接检验变化之差或目标终点组差。[Gelman与Stern关于显著性差异的原论文](https://sites.stat.columbia.edu/gelman/research/published/signif4.pdf)

交叉试验中同一人接受真/假刺激，模型需结合treatment、period、sequence、subject及设计对携带效应的处理。简单且适合的两条件比较可用配对分析，但不能一概忽略时期；两期设计也不保证同时识别所有携带参数。不要先检验携带效应、再按p值决定是否丢弃第二期。[Cochrane随机试验设计变体章节](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-23)

多个剂量或电场强度可以用连续回归、样条或GAM；个体实际电场与疗效的相关还可能受解剖等因素影响。刺激条件随机化不等于所有观察到的剂量/连接差异均随机化。ITT意向治疗是估计和分析原则，需要结合目标效应与缺失处理，不是写上标签就消除偏倚。

28. **调节、中介、SEM与因果推断**

调节moderation通常就是交互：

\[
E(Y)=\beta_0+\beta_1X+\beta_2Z+\beta_3XZ,\qquad
\frac{\partial E(Y)}{\partial X}=\beta_1+\beta_3Z.
\]

例如刺激效应是否随年龄变化，检验β₃，并报告不同年龄的条件效应及CI。对连续年龄随意分成两组会损失信息；两个亚组各自p值不同也不等于交互显著。

简单线性中介模型：

\[
M=aX+C\gamma+\varepsilon_M,\qquad
Y=c'X+bM+C\delta+\varepsilon_Y.
\]

在相应线性、无X×M交互等条件下，间接效应是ab，总效应c=c′+ab。乘積分布常偏斜，因此可用bootstrap、Monte Carlo或贝叶斯区间。总效应不显著不必然排除间接效应。

但“刺激→连接改变→行为改善”的因果解释需要时间顺序和无未测混杂等识别条件。刺激随机化不能自动解决中介—结局关系的混杂；显著ab并不直接证明脑机制。[Imai、Keele与Tingley因果中介原论文](https://imai.fas.harvard.edu/research/files/BaronKenny.pdf)

SEM把多条路径、潜变量与测量误差联合建模。常报告路径Wald z、整体χ²、df、CFI/TLI、RMSEA、SRMR。协方差SEM的df是独立协方差信息数减自由参数数：例如9个观测变量有9×10/2=45个独立协方差矩元素，估计21个参数时df=24；加入均值结构要重新计数。它不是OLS残差n−p。饱和模型df=0而完美拟合，并不证明理论正确。[lavaan CFA官方示例](https://lavaan.ugent.be/tutorial/cfa.html)

| 因果工具 | 作用 | 主要识别限制 |
|---|---|---|
| DAG | 明确因果假设，决定应调整什么 | 图由科学假设支持，不能仅用p值选箭头 |
| 倾向评分匹配/分层 | 平衡已观测处理前协变量 | 无未测混杂、重叠/正值性等仍重要 |
| IPW/IPTW | 用接受处理概率的倒数构建加权比较 | 极端权重与模型误设需处理 |
| g-computation | 建结局模型，预测不同处理下的反事实均值 | 依赖适当的结局模型与识别条件 |
| 双重稳健估计 | 结合处理模型和结局模型 | “其中一类模型正确”的稳健性不能消除未测混杂 |
| 工具变量IV | 借助影响处理而满足排除限制等的变量 | 有效工具的假设很强，弱工具影响推断 |
| Difference-in-differences | 比较暴露前后变化相对对照的差异 | 依赖平行趋势等条件，不等于任何组×时间分析都有因果性 |
| Regression discontinuity | 利用阈值附近的处理分配规则 | 连续性、阈值操纵等假设，效应通常是局部的 |

29. **贝叶斯分析：后验、可信区间、Bayes factor**

\[
p(\theta\mid y)\propto p(y\mid\theta)p(\theta).
\]

先验描述观测数据前对参数的约束，似然表达数据模型，后验结合两者。层级贝叶斯让个体估计向群体信息部分汇聚，适合重复、个体差异、规范模型与有效连接。

在指定模型和先验下，可以说“参数落在某后验可信区间中的概率为95%”。这不同于频率学95%置信区间的重复覆盖解释。后验预测检查用模型生成的数据与真实数据对照，评估模型是否能重现关键特征。

Bayes factor为：

\[
BF_{10}=\frac{p(y\mid H_1)}{p(y\mid H_0)}.
\]

分子分母是将参数按先验积分后的边际似然。BF衡量模型相对证据，不是p值，不直接等于H₁后验概率；后验优势比=BF×先验优势比。BF接近1往往说明区分力不足。备择先验选择会影响BF。[Rouder等贝叶斯t检验原论文](https://link.springer.com/article/10.3758/PBR.16.2.225)

MCMC和变分推断VI是近似计算后验的算法；R-hat、有效样本量、发散等属于计算诊断，不是研究效应的t/F。贝叶斯模型平均在多个模型间加权，反映模型不确定性；经验贝叶斯通常从数据估计部分先验/超参数，其不确定性处理需要说明。

30. **功效、样本量、等效性、非劣效性、序贯分析**

功效为真实效应等于某指定备择值时拒绝零假设的概率，即1−β。规划需要效应大小、噪声、个体内相关、α、检验方向、缺失和多重比较方案。复杂GAMM/NBS设计常用仿真：按设定机制生成数据，重复完整分析，计算拒绝比例；零效应下检查I类错误，备择下检查功效。[simr仿真功效官方教程](https://cran.r-project.org/web/packages/simr/vignettes/fromscratch.html)

不存在适用于所有脑影像问题的统一最小样本量。大规模脑—行为关联的小效应可能需要很大样本，不能直接用小样本中筛出的最大效应规划；干预、个体内和明确先验ROI的情形可能不同。[Marek等脑全域关联可重复性研究](https://www.nature.com/articles/s41586-022-04492-9)

阴性p值不能证明没有有意义的效应。等效检验TOST预先定义可忽略效应范围(L,U)，分别检验θ≤L和θ≥U；两项单侧检验都在α=.05拒绝时，典型均值问题等价于90%CI全部落在(L,U)内。统计显著和实际等效可以同时成立，例如极精确地发现一个很小的差异。[Lakens等效检验方法论文](https://journals.sagepub.com/doi/10.1177/1948550617697177)

非劣效检验只排除某个方向上差过预设幅度，不等同于双侧等效。序贯分析允许按事先设计查看累积数据，需采用相应的α消耗、边界或其他有效序贯方法；反复查看普通p<.05后随时停止会改变错误率。“观察功效”通常主要重述已得p值，阴性结果更应看效应区间和设计灵敏度。

31. **缺失数据与信度：统计分析的一部分**

| 方法/概念 | 解决的问题 | 解释重点 |
|---|---|---|
| MCAR | 缺失与观测和未观测值无关 | 较强假设 |
| MAR | 给定观测信息后，缺失不再依赖未观测值 | 常用于MI/似然分析的识别假设 |
| MNAR | 给定观测信息后，缺失仍依赖未观测值 | 需机制模型、模式混合或敏感性分析等 |
| MI/MICE | 多重插补缺失值，分析多份合理数据 | 合并参数及不确定性，不把份数当新样本 |
| FIML/观测数据似然 | 使用已观测部分的信息拟合模型 | 依赖正确模型与相应缺失假设 |
| ICC | 个体间变异相对总变异的比例/一致性 | 必须说明型号与CI |
| Cohen/Fleiss κ | 两个/多个评定者的分类一致性，扣除特定偶然一致基准 | 受类别比例和设计影响 |
| Bland–Altman | 看两次/两种测量的差值和一致性界限 | 补充r和ICC看不到的系统偏差 |

多重插补的Rubin合并规则为：

\[
\bar\theta=\frac1m\sum_j\widehat\theta_j,\quad
\bar U=\frac1m\sum_j U_j,\quad
B=\frac1{m-1}\sum_j(\widehat\theta_j-\bar\theta)^2,
\]

\[
T=\bar U+\left(1+\frac1m\right)B.
\]

T同时包含每份分析本身的不确定性与插补之间差异；合并t的SE为√T，df需Rubin/Barnard–Rubin等规则。均值填补、把多份插补数据拼大样本、或先平均各份数据再分析，都会遗漏必要的不确定性。[MICE pool官方文档](https://amices.org/mice/reference/pool.html)

简单随机截距模型中：

\[
ICC=\frac{\sigma^2_{\mathrm{between}}}
{\sigma^2_{\mathrm{between}}+\sigma^2_{\mathrm{within}}}.
\]

但实际ICC有单/双向、绝对一致/一致性、单次/多次平均等型号。两次测量如果所有人第二次都高10分，Pearson r可能为1，却并非绝对一致。应报告ICC定义和CI，并注意样本异质性会改变ICC。[Koo与Li的ICC报告指南及勘误入口](https://pubmed.ncbi.nlm.nih.gov/27330520/)

32. **元分析：效应量合并和坐标汇聚不是一回事**

效应量元分析将各研究估计θ̂ᵢ和研究内方差vᵢ合并：

\[
\widehat\mu=\frac{\sum_iw_i\widehat\theta_i}{\sum_iw_i}.
\]

共同效应常用wᵢ=1/vᵢ；随机效应常用wᵢ=1/(vᵢ+τ̂²)，τ²描述研究间真实效应方差。多层/稳健元分析可处理同一研究多个相关效应，meta-regression研究研究层特征，网络元分析结合多种干预的直接与间接比较并需要可传递性/一致性等假设。

经典同质性检验：

\[
Q=\sum_i\frac{(\widehat\theta_i-\widehat\mu_{\mathrm{FE}})^2}{v_i},
\qquad df=k-1.
\]

常规条件下与χ²(k−1)比较。常见Q定义的I²估计为max[0,(Q−(k−1))/Q]×100%；其他实现可基于τ²与典型研究内方差，不能把这当成唯一算法。合并均值CI不等于新研究效应的预测区间；漏斗图不对称也不只由发表偏倚造成。[Cochrane元分析官方章节](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-10)

ALE检验跨实验激活坐标是否空间汇聚；MKDA以实验层核密度等方式整合空间证据；SDM类方法重建并整合带方向的效应图，各自细节不同。它们不能无条件替代完整统计图或原始效应量元分析。同实验的多个峰、同一样本的多个contrast不能当成独立研究。[Eickhoff等ALE修订方法论文](https://pubmed.ncbi.nlm.nih.gov/21963913/)

33. **特定研究还会遇到的模型**

| 方法 | 脑科学用途 | 主要统计输出或限制 |
|---|---|---|
| Kaplan–Meier / log-rank | 刺激后多久复发、认知障碍多久转化 | 生存曲线/生存分布比较；处理删失而非删除未发生事件者 |
| Cox比例风险 | 生存结局与脑指标、治疗及协变量关系 | HR、Wald/score/LRT；检查比例风险等假设 |
| AFT加速失效时间 | 对事件时间本身的加速/减速建模 | 时间比，与HR解释不同 |
| 竞争风险/联合模型 | 多种互斥事件，或纵向脑指标与事件时间联合分析 | 明确目标是何种风险或事件过程 |
| 心理测量函数 | 刺激强度与检出/辨别概率 | 阈值、斜率、猜测/失误率及区间 |
| DDM/HDDM | 同时解释选择与反应时 | 漂移率、边界、起点、非决策时间；层级后验 |
| 强化学习模型 | 学习、奖励预测误差与脑信号/刺激效应 | 学习率、价值、选择温度；检查参数恢复与预测 |
| 圆形统计 | 相位、方向、周期变量 | 圆均值、合向量长度、Rayleigh/圆相关等 |
| 空间回归/空间GP | 明确把空间相关写进均值或协方差模型 | 参数及空间不确定性，需检查残差空间结构 |
| 潜在类别/混合模型 | 用概率模型描述异质群体或状态 | 类别概率与模型选择；聚类不自动等于真实病理亚型 |

Cox常写h(t|X)=h₀(t)exp(Xβ)，exp(β)是条件HR；HR不是风险比，也不必是生存时间比。[R survival coxph文档](https://stat.ethz.ch/R-manual/R-devel/library/survival/html/coxph.html)

DDM将反应时和选择分解为模型化认知过程；漂移率等不是直接观察到的心理实体，需要参数恢复、可识别性和预测检查。[Wiecki等HDDM原论文](https://www.frontiersin.org/journals/neuroinformatics/articles/10.3389/fninf.2013.00014/full)

圆形变量1°和359°的平均方向接近0°，普通算术平均却是180°；因此需要专门统计。圆形统计的R/平均合向量长度是集中程度，不是回归R或R²，Rayleigh z也不是标准正态z。[Berens圆形统计工具箱论文](https://www.jstatsoft.org/article/view/v031i10)

34. **把研究问题映射到一套完整分析**

| 具体研究问题 | 起点模型/估计 | 检验与报告 |
|---|---|---|
| 两组一个预先指定ROI的连续指标差异 | Welch t，或调整协变量的GLM | 均值差、CI、t(df)、p；有多个ROI时定义校正 |
| 控制年龄等后，脑指标与行为是否相关 | GLM/偏相关 | β、partial r或partial R²、CI、t(df) |
| 年龄与网络指标是否呈曲线 | GAM | 曲线与CI、edf/Ref.df、平滑F/χ²；单独定义非线性检验 |
| 重复MRI的非线性发育轨迹 | GAMM | 固定曲线、个体随机效应、模型检验与拟合诊断 |
| 真/假刺激一个主要随访终点 | 基线调整ANCOVA | τ及CI、t；效应单位与主要终点 |
| 真/假刺激多次随访 | LMM/MMRM，必要时GAMM | 指定组×时间或随访contrast、df估计方法 |
| 二分类应答与组别关系 | χ²/Fisher，或logistic调整协变量 | 应答率、RD/RR/OR、CI、χ²或Wald/LRT |
| 全脑任务效应 | 一层/二层GLM | contrast、t/F、df、voxel/cluster/TFCE和校正范围 |
| 全连接组组间差异 | 边级GLM+FDR/maxT，或NBS | 边级或分量级结论必须匹配方法 |
| 两张皮层图的空间对应 | Pearson/Spearman+空间零模型 | r、空间经验p、代理图匹配与多重校正 |
| 多脑特征与多行为的共同模式 | CCA/PLS | 成分、置换显著性、稳定性、样本外验证 |
| 预测新受试者刺激疗效 | 正则化/CPM等+嵌套CV/外部验证 | R²_test、MAE/RMSE、r或分类指标、CI/置换 |
| 证明两方案差异足够小 | TOST | 预设等效界值、相应CI、两个单侧检验 |
| 脑指标是否可靠 | 适当ICC+Bland–Altman等 | 型号、估计、CI、系统偏差和误差范围 |

35. **读一篇论文时逐项核对什么**

读方法与结果时，按以下顺序提问，可以把大部分缩写放回正确位置：

1) 因变量是什么：BOLD contrast、Fisher-z FC、FA、网络效率、事件数、诊断，还是预测误差？
2) 独立单位是什么：人、家系、中心、试次、时间点、节点，还是研究？记录条数是否被误当作独立样本？
3) 模型是什么：一般GLM还是广义GLM，LMM还是GAMM？分布、链接、固定/随机项如何定义？
4) 科学零假设是什么：单个β、组别整体、交互、曲线整体、非线性部分、子网、等效界值？
5) 统计量怎么来：估计/SE的t或z、嵌套模型F、列联表χ²、LRT，还是经验置换分布？
6) df是什么：n−rank(X)、分子/分母df、近似混合模型df、edf/Ref.df，还是SEM约束数？
7) 效应有多大：未标准化差异、r、partial r、ΔR²、partial R²、OR等；是否有CI？
8) 多重比较控制什么：FWER还是FDR，family多大，位置/簇/分量哪一层，是否覆盖多个contrasts？
9) 模型是否支持解释：残差、异方差、相关结构、影响点、共线性/共曲性、分离、随机效应奇异拟合、缺失机制和空间null是否检查？
10) 若是预测或高维模式：训练/测试是否分离，特征选择和调参是否在训练内，是否报告留出性能和稳定性？

例如结果“t(95)=4.87，partial r=.447，p_FDR=.012”包含的是：统计量、参考df、单个目标变量的调整后关联大小、以及某一检验家族中的FDR调整p。它不单凭这行说明原始β单位、因果性、全模型R²或预测性能。

最后用三个模型写法巩固阅读顺序：独立连续结局从 y~group+age+covariates 理解一般GLM；有重复记录加入受试者随机效应理解LMM；年龄可能弯曲时将线性age替换为s(age)理解GAM，二者合用形成GAMM。每一步都重新明确目标contrast、合适的SE/df、效应量和多重比较方案。