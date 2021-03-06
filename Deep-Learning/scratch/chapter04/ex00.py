# 오차 역전파 (backpropagation)
# 가중치 매개변수의 기울기를 효율적으로 계산
# 수식을 통한 방법, 계산 그래프를 통한 방법 두가지가 있다 

# 계산 그래프 : 계산 과정을 그래프로 나타낸 것
# 복수의 노드(node) 와  에지(edge: 노드 사이의 직선)

# 계산을 할때 왼쪽에서 오른쪽으로 진행하는 방법 forward propagation 순전파 
# 순전파의 반대 방향 으로 진행하는 방법 back propagation 역전파 

# 국소적 계산 : 
# 전체 계산이 아무리 복잡하더라도 각 단계에서 하는 일은 해당의 노드의 국소적 계산이다 

# 계산 그래프로 푸는 이유 
# 1. 국소적 계산 : 전체가 아무리 복잡해도 각 노드에서는 단순한 계산에 집중하여 문제를 단순화 
# 2. 계산 그래프는 중간 계산 결과를 모두 보관할 수 있다 

# 연쇄법칙 (국소적 미분)
# : 계산 그래프 상의 역전파와 같다
# 합성 함수 (여러 함수로 구서오딘 함수)의미분에 대한 성질 

# 역전파 
# 덧셈 노드의 역전파 
# 곱셈 노드의 역전파 (순전파의 입력 신호를 변수에 저장 )