## Základní paradigmata dobývání znalostí
- Data preparation
	- Selection
	- Preprocessing
	- Transformation
- The actual "Data mining"
	- Apply chosen analytical methods to search for interesting relationship among the data
	- Respective methods can be applied multiple times
	- Results of previous runs may impact the actual parameters of the following runs
	- The respective types of methods can be combined based on obtainer partial results
- Interpretation
	- The found knowledge shall be evaluated from the point of view of the end user

#### From a point o view of a manager
- Form a team of professionals
- Specify the problem
- Obtain all the data available
- Select the method/s
- Preprocess the data
- Mine the data
- Interpret the results

#### Tasks for Data mining
- Classification and prediction
	- The objective is to find knowledge aiding to classification of new patterns
	- The obtained knowledge should reflect the underlying concept as well as possible
	- We gain more knowledge that can be challenging to interpret
- Description
	- The objective is to find a dominant structure or relationships contained in the given data
	- We demand an easy to understand knowledge that fully covers the given concepts
	- We obtain a smaller amount of less precise knowledge
- Looking for "nuggets"


## Příprava dat
- Data standardization
	- Decimal scaling to the interval [-1,1] - divides the attribute values by the smallest power of 10
	- Range standardization to the interval [0,1] normalizes attribute values: x\_if - min(f) / (max(f) - min(f))
	- z-score standardization - mean 0, absolute deviation 1
	- standard deviation standardization - mean 0, standard deviation 1
	- log transform
- Nominal attributes
	- Transform to binary attributes (v binary-valued attributes)
- Ordinal attributes
	- Like a nominal, but its values have a numerical ordering (e.g. Young MiddleAge, Old)
- Goals
  - Select (or create) from the available data those ones relevant for the data mining task at hand
  - Represent this data in a form suitable for processing by the chosen algorithm
  - Final state = data table containing the attribute values of the objects
- Structured data
  - Temporal data
    - E.g. time series of stock prices
    - Typical task to predict future values
  - Spatial data
    - E.g. geographic information systems
    - An implicit neighborhood relationship
  - Structural data
    - E.g. chemical compounds
- Data with too many objects
  - Use a sample of objects
  - Or use a way to store the data without necessity to save them to RAM
  - Or build more models based on subsets of data
  - Selected objects should capture the nature of the data as best as possible
- Data with too many attributes
  - Reduce amount with expert
  - Automatic reduction
    - Transformation (e.g. PCA analysis)
      - Necessity to provide the values of all original attributes
      - New attributes might lack a clear interpretation
  - Selection
    - Filter methods
      - to each of the attributes, computes a characteristics that reflects contribution to classification
      - Criteria based on contigency tables
      - Probability estimation
      - X^2
      - Entropy H(A)
      - Information measure of dependence
    - Wrapper methods
      - Use a machine learning algorithm to build a model using a subset of attributes, use the best models
- Numeric attributes
  - Discretization
    - Division to intervals
  - Fuzzy discretization
    - Boundaries of fuzzy-intervals are 'blurry'
- Categorical attributes
  - Algorithm to group them together (KEX)
- Missing values
  - Ignore objects with any of the values missing
  - Replace the missing value by 'I don't know'
  - Replace the missing value by an existing attribute value
    - The most frequent value
    - Proportional to the ratio of all values
    - Any value
  - Completion by means of (a used) model

## Výběr atributů a metody pro analýzu jejich relevance
- Range, quartiles, and outliers
	- Interquartile range = Q3 - Q1
	- Outliers - greater than Q3 + 1.5 interquartile range; less then Q1 - 1.5 interquartile range
- Contigency table
	- řádky X1, 2, 3, ..., sloupce Y1, 2, 3, ..., buňky frequency of combination
	- e\_kl - expected frequency of combination when assuming independence of X and Y (r\_k * s\_l / n)
- X^2-test
	- součet přes všechny buňky (a\_kl - e\_kl)^2 / e\_kl
	- Pokud X^2 >= konstantně X^2\_(R-1)(S-1) pro danou significance, např. 0.05, tak dependence platí
	- Použitelné pouze pokud pro všechny k, l: (r\_k * s\_l) / n >= 5
- Fisher's-test
	- a\_11 = min a\_kl
	- P = suma od 0 do a\_11: (r\_1! r\_2! s\_1! s\_2!) / (n! (a\_11 - i)! (a\_12 + i)! (a\_21 + i)! (a\_22 - i)! )
	- if P <= alpha, they are dependent



## Metody pro dobývání znalostí
#### SEMMA
- Sample - select data for modeling, may include data sampling, partitioning, ...
- Explore - visual exploration of the data and its reductions, involves data visualizing techniques (outlier detection, clustering methods, ...)
- Modify - prepare (select, create and transform) the objects
- Model - application of various data mining techniques (decision trees, regression, neural networks, ...)
- Assess - evaluate the results of modelling for their reliability and usefulness

#### CRISP-DM
- Business understanding
	- Determine business objectives
	- Assess your present situation - inventory of resources, necessities, assumptions, problems, risks, opoortunities, possibilities, costs and benefits
	- Determine goals and criteria for business success
	- Develop your project plan
- Data understanding
	- Collect initial data
	- Describe the data
	- Explore data and visualize it
	- Verify the quality of the data
- Data preparation
	- Data selection, cleaning, construction (derived attributes, generated records), integration (merged data), aggregation (summarizing data), formatting
- Modeling
	- Select the modeling technique
	- Generate test design
	- build the model (iteratively)
	- Assess the model - evaluate results, rank them, ...
- Evaluation
	- Evaluate the results (from the point of view of the manager)
	- Review the process
	- Determine subsequent steps
- Deployment
	- The results shall be presented in the form easy to interpret and deploy by the user
	- Plan deployment
	- Monitor the plan and its maintenance
	- Produce the final report
	- Review the project - document the experiment - difficulties and wrong approaches, hints for choosing the best techniques and practices

#### ASUM-DM
Because of need of Project management  
Scalable and enterprise-ready  

- Analyze
- Design
- Configure & Build
- Deploy
- Operate & Optimize
- +Project management


## Asociační pravidla, přístupy založené na principu učení s učitelem a klastrová analýza
#### Market Basket Analysis
- How to do that
  - Item
  - Transaction contains one or mroe items
  - Frequency table
    - How many times were there two products purchased together
    - Diagonal = how many times the item was purchased overally
  - Support of the rule
    - How often can we use the rule - #transations that contain i and j / #all transactions
  - Confidence
    - How reliable are the results of the rules - #transactions that contain i and j / #transactions that contain i
  - Lift
    - p(i and j) / p(i)p(j)
    - if lift < 1: rule is worse than random choice -> IF condition THEN NOT conclusion
- Tips
  - In the beginning, use more general items
  - Later, generate rules for specific items based only on the transactions that contain these items
  - Move rare items to higher levels in the taxonomy (where they appear relatively mroe frequently)
  - Leave the more common items at lower levels (in order to not allow the most frequent items to dominate the rules)
- Virtual items
  - E.g. company brands
- Pruning
  - Elemination of rare items
  - Or use a taxnomy to create general items
- APRIORI algorithm
  - Combinations that reach `minsup` support
  - When loking for combinations of the length k, we use the known combinations of the length k-1 -> breadth-first generation of combinations
  - To generate combinations of the length k, we demand all their sub-combinations of the length k-1 to fulfill the preset frequency requirement
- Dissociation rules
  - IF A AND NOT B THEN C
  - Twice as many items, increased size of transactions, negated rules occur more often
- Time-series analysis
  - Cause-effect analysis
- Mining Class association rules (CAR)
  - Transactions are albeles with a class (e.g. Student, Teach, School: Education)
  - Class assiciation rule is an implication X -> y
  - Can be mined in one step - find all rule-items with a support above minsup
- FP-Growth
  - Build a compact data structure FP-tree
  - Extracts frequent itemsets directly from the FP-tree
  - V podstatě "trie" (pozn. itemy v transakci jsou seřazeny abecedně) s tím, že se udržujou pointery k nodům stejného itemu (který je v jiné branchi)
  - extrakce itemsetů jde odspoda
    - Např. nejdřív itemsety s `e`, pak s `de`, `ce`, `be`, `ae`

#### Bayesian Classification
- Bayesian formula
  - P(H|E) = P(E|H)P(H) / P(E)
- Most Probable hyptohesis H_MAP
  - H_MAP = H_J
  - P(E|H_J)P(H_J) = max over t (P(E|H_t) / P(H_t))
  - Např. klient with a high income.
    - P(HIGH_INCOME|BORROW)P(BORROW) = 0.607
    - P(HIGH_INCOME|REJECT)P(REJECT) = 0.040
    - -> H_MAP = BORROW
- Naive Bayes
  - respective events E_1, ..., E_kK are conditionally independent
  - P(H|E_1, ..., E_K) = P(E_1, ..., E_K|H)P(H) / P(E_1, ..., E_K)
  - P(E_1, ..., E_K|H) se pořítá jako součin k=1 to K (P(E_k|H))
  - Příklad: klient middle balance, not unemployed:
    - P(Credit(Yes)) * P(Accont(Middle)|Credit(Yes)) * P(Unemployed(No)|Credit(Yes)) = 0.1042
    - To stejné akorát s Credit(no)
    - Vyber větší pravděpodobnost

#### SVM
- Support Vector Machines
- Separovat 2 třídy pomocí hyperplane s co největším marginem
- Optmalizační problém
- Násobení vektorů/matic
- Lagrange multiplies
- KKT (Kuhn-Tucker conditions)
- Duální formulace
- Nelineární separace pomocí Kernal functions
  - Polynomial kernel (x^2*z^2, xz, ...)
  - Kernel trick (něco jako infinite kernel, aniž by byl explicitní?)

#### Decision Trees
- Difficult to process continuous data
- Difficult to process for missing data
- TDIDT (top down induction of decision trees)
  - Divide and rule
  - Choose one attribute as a root of the patrial subtree
  - Divide the data arriving at this node into subsets according to the values of the chosen attribute and add a node for each subset
  - If there is a node such that the data arriving at it do not belong all to the same class, repeat the process for it starting form step 1
  - Choice of an attribute
    - Entropy (measure of disorder in the system)
    - H = - sum_t=1 to T (p_t log_2(p_t))
  - Řekněme
    - Income high: loan approved 5, loan not approved 0
    - Income low: loan approved 3, load not approved 4
    - H(INCOME) = 5/12 H(INCOME(HIGH)) + 7/12 H(INCOME(LOW))
    - H(INCOME(LOW)) = - (3/7 log(3/7) + 4/7 log(4/7))
    - Spočítá se H(každý z atributů), ten s nejnižší entropií se vybere
- Pruning
  - Replacement by most frequent class
  - Must not perform worse on the validation set
- ID3
  - Information gain
  - binary values
- Gini-index 
  - Check all the possible values to split to right and left subtree, use gini-index
- Bagging
  - Bootstrapped aggregating
  - Independent and identically distributed classifiers
  - Uniformly sample from original data (with replacement)
  - k different classifiers -> random forests
  - Random forests use also limited number of featurech (at each node)
  - Not immune to bias
  - Majority vote
- Boosting
  - Weigth is associated with each training pattern
  - Weigths of patterns are iteratively modified based on the performance of classifier
  - AdaBoost
    - Sequence of classifiers
    - Each classifier depends on the previous one (focuses on the previous one's errors)
    - Incorrectly predicted examples are given higher weights

#### Cluster analysis
- Divide the observed patterns into clusters
- Manhattan distance, Euclidean distance, Chebyshev distance (maximum rozdílu přes dimenze)
- Minkowski metrics = z-tá odmocnina z sumy přes dimanze (x\_1j - x\_2j)^z
- Normalize quantities -> assume the same variance
	- Different variance for the quantities - Mahalonobis distance
- Distance between 2 clusters U and V:
	- nearest neighbor
	- farthest neighbor
	- average distance
	- centroid distance
- Clustering by means of the k-means method:
	- Divide randomly into k clusters
	- Determine the centroid of all the clusters in recent division
	- For each x, determine distance to all centroids
		- If x does not belong to closest cluster, move it
	- If there was a transfer, repeat
- Hierarchical clustering
  - Determine mutual distances between all
  - Assign each to individual cluster
  - While there are more clusters
    - Find two mutually clasest clusters and merge them
    - Compute distance to other clusters
  - Dendrogram shows gradual merging
- Vector quantization - LVQ
- k-medoids
  - Find k representatives to minimize objevtice function - sum of distances between data points and their closest representative
  - Perform exchanges some representative <-> data point to improve as much as possible
    - hill-climbing to find
- CLARANS
  - scalabel k-medoids


## Metody pro extrakci charakteristických diskriminačních pravidel a měření jejich zajímavosti
- Regression analysis
	- Determine the relationship of variable Y to other (one or more) variables X\_1, ..., X\_n
	- Linear regression
	- Least squares method
	- Multi-dimensional regression linear or logistic
- Discriminant analysis
	- Classification of patterns into known classes
	- Linear discriminant analysis - discrimination into two classes


## Reprezentace, vyhodnocování a vizualizace získaných znalostí
- Metriky
  - Accuracy = # of correct classifications / # of test cases
  - Efficiency
    - Time to contruct the model
    - Time to use the model
  - Robustness
    - Handling noise and missing values
  - Scalability
    - Efficiency in disk-resident databases
  - Interpretability
    - Clarity and insight provided by the model
  - Compactness of the model
- Holdout set (test set)
  - Rozdělení dat na training set a test set
  - n-fold cross-validation
    - Kdy je málo dat
    - rozdělení dat na n stejně velkých disjoint setů
    - Pro každý set: dá daný set jako test set s tím, že zbytek je training set
    - Když se to takhle udělá n-krát, tak n accuracies -> average
- Validation set
  - Rozdělení na training set, validation set (během učení např. po každé epoše, pro odhad, kdy je to ok, finetunování hyperparametrů apod.), test set (jenom na konci učení)
- Precision and recall
  - True positive = # of correct classification of positive examples
  - False negative = # kdy jsme řekli negative, ale ve skutečnosti byo positive
  - False positive = # kdy jsme řekli positive, ale ve skutečnosti bylo negative
  - True negative = # of correct classification of negative examples
  - Precision = TP / (TP + FP)
    - Correctly classified / total examples classified as positive
  - Recall = TP / (TP + FN)
    - Correctly classified positive examples / total actual positive examples
  - F1-score = 2pr / (p+r)
    - precision i recall musí být vysoké pro co nejvyšší F1-score
- Scoring and ranking
  - Scoring - probability estimate (PE) že example patří do positive class
  - Rank exampes by PE
  - Then divide to n bins. Nakresli z toho lift curve
- ROC-curve
  - Receiver Operating Characteristic curve
  - TPR = TP / (TP+FN)
    - fraction of actual positive cases that are correctly classified
  - FPR = FP / (TN+FP)
    - fraction of actual negative cases classified to positive class
  - Pro porovnání různých classifierů se používá area under ROC curve


## Modely pro analýzu sociálních sítí
- Graph
- Edges directed/undirected, possibly with weights
- Linear threshold model
	- A node would take an action if the % of his friends who have taken action exceeds a certain threshold 
- Independent Cascade Model
	- Node, upon activation, has one chance to activate each of its neighbors randomly
- Schelling Model of Segregation
	- Example how immutable characteristics can become highly correlated with mutable characteristics
	- In each round, first satisfy all unsatisfied agents
	- Then all unsatisfied agents move to a location where they are satisfied
	- If can't find a new location - leave alone or move to random location
	- Self-imposed segregation
- Link analysis - HITS, PageRank
	- Update each node's PageRank by applying: divide the actual PageRank value of page by the number of its outgoing links and pass these equal shares to the pages it points to.
	- The update of a node's PageRank value is performed by summing the shares it receives in each iteration


## Míry centrality, detekce komunit
#### Míry centrality
- Degree centrality
	- Node's in- and out- degree
- Betweenness centrality
	- Number of shortest paths passing through a node divided by all shortest paths in the network
	- Pro vrchol v, vem si všechny dvojice i, j, které prochází vrcholem v jako nejkratší cestou, vyděl 1 / <počet nejkratších cest mezi i, j>, a sečti napříč všemi dvojicemi i, j
- Closeness centrality
	- 1 / (avg. length of shortest paths to all other nodes in the network)
- Eigenvector centrality
	- Proportional to the sum of eigenvector centralities of all nodes directly connected to given node
	- Similar to PageRank
	- "How well is this person connected to other well-connected people?"
- Node's clustering coefficient (density of its neighborhood)
- Average and longest distance

#### Community detection
- Minimum-Cut
	- Divide the network into two communities by minimizing the number of edges running through unlike groups
- Girvan-Newman algorithm
	- Identify bridges, using edge betweenness
	- Compute betweenness
	- Remove edges with highest betweenness
	- Repeat until no edges to remove
	- To select best division, compute modularity (it's about the number of edges between communities) of each network's division.
- Louvain algorithm
	- Each node a single community
	- Compute modularity Q
	- Move the isolated mode from its community to a neighboring community
	- Compute the gain/loss in modularity yielded by changed assignment
	- If modularity increases, keep the node in "new" community
	- Repeat until no further improvements possible
	- Create a new network, derived from the original one, where each new node is the aggregation of the nodes assigned to a given community
	- Repeat all until maximum of modularity is attained
- Agglomerative hierarchical clustering
	- Initialize each node as a community
	- Merge communities successively into larger communities following certain criterion (e.g. modularity increase)


## Praktické využití technik pro dobývání znalostí a analýzu sociálních sítí.
#### Sociální sítě
- Bussinesses
	- Analyse and improve communication flow in organization, with partners or customers
	- Marketing campaign based on social networking
- Social network sites
	- Identify and recommend potential friends based on friends-of-friends
- Network operators
	- Optimize the structure and capacity of communication networks
- Medicine
	- Sexually transmitted diseases
	- Vaccination campaigns (hubs- people with many cantacts) 
	- New drugs (targeting key molecules)
- Networks with a Scale-free architecture
- Analysis of webpages, internet traffic, dezinformation spread through mail

#### Data Mining
- Segmentation and classification of bank/insurance company clients clients (e.g. dataction of problematic or creditworthy clients)
- Analysis of the causes of failures in telecommunication networks
- Analysis of the causes of a change of service provider
- Prediction of power consumption
- Prediction of stock price evaluation
- Analysis of the patient database in a hospital
- Market basket analysis - search for relationship between different types of goods
