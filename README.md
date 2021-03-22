# algorithm_study

* [스택](#스택)
* [큐](#큐)



# 스택
<details>
  <summary> 문제1 </summary>
  
  1. 문제 설명
  ~~~
    주식가격
    문제 설명
    초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

    제한사항
    prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
    prices의 길이는 2 이상 100,000 이하입니다.
    
    입출력 예
    prices	return
    [1, 2, 3, 2, 3]	[4, 3, 1, 1, 0]
    
    입출력 예 설명
    1초 시점의 ₩1은 끝까지 가격이 떨어지지 않았습니다.
    2초 시점의 ₩2은 끝까지 가격이 떨어지지 않았습니다.
    3초 시점의 ₩3은 1초뒤에 가격이 떨어집니다. 따라서 1초간 가격이 떨어지지 않은 것으로 봅니다.
    4초 시점의 ₩2은 1초간 가격이 떨어지지 않았습니다.
    5초 시점의 ₩3은 0초간 가격이 떨어지지 않았습니다.
  ~~~
  2. 소스코드
  ~~~
    package stack;

    import java.util.Arrays;
    import java.util.Stack;

    class Solution {
        public int[] solution(int[] prices) {
            Stack<Integer> beginIdxs = new Stack<>();
            int i=0;
            int[] terms = new int[prices.length];

            beginIdxs.push(i);
            for (i=1; i<prices.length; i++) {
                while (!beginIdxs.empty() && prices[i] < prices[beginIdxs.peek()]) {
                    int beginIdx = beginIdxs.pop();
                    terms[beginIdx] = i - beginIdx;
                }
                beginIdxs.push(i);
            }
            while (!beginIdxs.empty()) {
                int beginIdx = beginIdxs.pop();
                terms[beginIdx] = i - beginIdx - 1;
            }

            return terms;
        }
    }
    
    answer를 prices의 길이 n으로 맞춰줍니다.
    스택 st를 생성합니다. st는 시간을 쌓습니다.
    0초부터 n-1초까지 순회합니다.
    st이 비지 않고, 만약 st의 가장 마지막 원소 top이 현재 주식 가격보다 크다면 다음을 반복합니다.
        스택에서 가장 마지막에 저장된 시간 top을 빼냅니다.
        answer[top]에 현재시간 i 와 top의 차를 저장합니다.
    st에 현재 시간 i를 저장합니다.
    
    스택이 빌 때까지 다음을 반복합니다.
        스택에서 가장 마지막에 저장된 시간 top을 빼냅니다.
        answer[top]에 끝 시간 n-1 과 top의 차를 저장합니다.
    이렇게 초기화된 answer를 반환합니다.

  ~~~
  3. 추가 설명
  ~~~
    문제에서는 1초, 2초, .. 5초로 표현했지만, 저는 배열 인덱스를 맞추기 위해서 0초, 1초, ... 4초로 표현하도록 하겠습니다. 이제 0초 때, 주식 가격이 얼마나 유지되었는지를 살펴보죠,

 
    0초:
    가격 : prices[0] = 1
    유지 시간 : 4초
    0초때는 그 이후로 현재 주식가격 1보다 떨어지는 주식이 없습니다. 즉 그 이후로 계속 유지 된다는 것이죠. 이제 각 초를 살펴보죠.

    1초:
    가격 : prices[1] = 2
    유지 시간 : 3초
    1초 때 역시, 이 이후로, 현재 가격 2보다 떨어지지 않습니다.

    2초:
    가격 : prices[2] = 3
    유지 시간 : 1초
    2초 떄는 현재 가격 3에서 1초 후, 3초에서 2로 떨어집니다. 그래서 유지 시간은 1초입니다.

    3초:
    가격 : prices[3] = 2
    유지 시간 : 1초
    3초때 역시, 이 이후로 떨어지지 않습니다. 남은 시간 1초간 유지됬다고 생각하면됩니다.

    4초:
    가격 : prices[4] = 3
    유지 시간 : 0초
    마지막 시간 4초 때는 유지 시간이 없는걸로 칩니다. 즉 0초이지요. 



    현재 시간 : 0초
    st = [0]

    이제 1초 후입니다. 먼저 현재 시간의 주식가격과 스택 st에 저장된 마지막 시간의 주식 가격을 비교합니다.

    현재 시간 : 1초
    st = [0]
    prices[1] = 2 > prices[0] = 1
    만약 현재 주식 가격이 크다면, 스택에 저장합니다.



    현재 시간 : 1초
    st = [0, 1]
    2초 역시 1초 떄까지와 마찬가지로 현재 시간의 주식가격과 스택에 저장된 마지막 시간의 주식가격을 비교합니다. 현재 주식가격이 크군요. 따라서 스택에 그 시간을 저장합니다.



    현재 시간 : 2초
    st = [0, 1, 2] (prices[2] > prices[1])
    3초 때를 비교해봅시다. 현재 주식가격보다, 스택에서 마지막에 저장된 시간의 주식가격이 더 큽니다.


    현재 시간 : 3초
    st = [0, 1, 2]
    prices[3] = 2 < prices[2] = 3
    이 때는, 스택에서 마지막 시간을 빼온 후, 현재 시간 - 마지막 시간, 즉 유지 시간을 구합니다. 
    st = [0, 1] //2 빠짐
    answer[2] = 3 - 2 // 유지 시간
    
    반복해서, 현재 시간의 주식가격과 스택에 저장된 마지막 시간의 주식가격을 비교합니다.
    현재 시간 : 3초
    st = [0, 1]
    prices[3] = 2 == prices[1] = 2

    가격이 같기 때문에, 현재 시간을 저장합니다.
    현재 시간 : 3초
    st = [0, 1, 3]
    즉, 스택에 저장된 마지막 시간의 주식 가격이, 현재 주식 가격보다, 크다면, 주식 가격은 유지하지 못한것입니다.
    따라서, 시간이 지날 때마다, 스택에 저장된 마지막 시간의 주식 가격이 현재 주식 가격보다 작거나 같은 가격이 나올 때까지 스택에서 빼온 후, 
    해당 유지 시간, "현재 - 마지막에 저장된 시간"을 answer의 마지막에 저장된 시간 위치에 저장하면 됩니다.



    이제 4초 때입니다. 스택에서 저장된 마지막 시간의 주식 가격과, 현재 주식 가격을 비교합니다.
    현재 시간 : 4초
    st = [0, 1, 3]
    prices[4] = 3 > prices[3] = 2
    따라서, 스택에 현재 시간을 저장합니다.
    현재 시간 : 4초
    st = [0, 1, 3, 4]


    이제 첫 시간 0초부터 마지막 시간 4초까지 유지한 숫자들이 스택에 최종적으로 남습니다. 그래서, 이제 스택에서 빼오면서, 유지 시간(최종 시간 - 저장된 시간)들을 구하면 됩니다.
    answer[스택 저장된 시간] = 최종 시간 - 스택 저장된 시간
    answer[4] = 4-4 = 0
    answer[3] = 4-3 = 1
    answer[1] = 4-1 = 3
    answer[0] = 4-0 = 4


    이렇게 하면 답 answer를 구할 수 있습니다.



    answer = [4, 3, 1, 1, 0]

  ~~~
</details>

# 큐
<details>
  <summary> 문제1 </summary>
  
  1. 문제 설명
  ~~~
    문제 설명
    트럭 여러 대가 강을 가로지르는 일 차선 다리를 정해진 순으로 건너려 합니다. 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 합니다. 
    트럭은 1초에 1만큼 움직이며, 다리 길이는 bridge_length이고 다리는 무게 weight까지 견딥니다.
    ※ 트럭이 다리에 완전히 오르지 않은 경우, 이 트럭의 무게는 고려하지 않습니다.

    예를 들어, 길이가 2이고 10kg 무게를 견디는 다리가 있습니다. 무게가 [7, 4, 5, 6]kg인 트럭이 순서대로 최단 시간 안에 다리를 건너려면 다음과 같이 건너야 합니다.

    경과 시간	다리를 지난 트럭	다리를 건너는 트럭	대기 트럭
    0	  []	      []	  [7,4,5,6]
    1~2	[]	      [7]	  [4,5,6]
    3	  [7]	      [4]	  [5,6]
    4	  [7]	      [4,5]	[6]
    5	  [7,4]	    [5]	  [6]
    6~7	[7,4,5]	  [6]	  []
    8	  [7,4,5,6]	[]	  []
    따라서, 모든 트럭이 다리를 지나려면 최소 8초가 걸립니다.

    solution 함수의 매개변수로 다리 길이 bridge_length, 다리가 견딜 수 있는 무게 weight, 트럭별 무게 truck_weights가 주어집니다. 
    이때 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 return 하도록 solution 함수를 완성하세요.

    제한 조건
    bridge_length는 1 이상 10,000 이하입니다.
    weight는 1 이상 10,000 이하입니다.
    truck_weights의 길이는 1 이상 10,000 이하입니다.
    모든 트럭의 무게는 1 이상 weight 이하입니다.
    
    입출력 예
    bridge_length	  weight	truck_weights	                    return
    2	              10	      [7,4,5,6]	                        8
    100	            100	      [10]	                            101
    100	            100	      [10,10,10,10,10,10,10,10,10,10]	  110
  ~~~
  
  2. 소스코드
  ~~~
    import java.util.*;

    public class Truck_Solution {
        public int solution (int bridge_length, int weight, int[] truck_weight){
            int answer = 0;
            Queue<Integer> q = new LinkedList<>();
            
            int max = 0;
            for(int w : truck_weight){
                while(true){
                    if(q.isEmpty()){
                        q.offer(w);
                        max += w;
                        answer++;
                        break;
                    }
                    
                    else if (q.size() == bridge_length){
                        max -= q.poll();
                    }
                    
                    else {
                        if(max + w > weight){
                            q.offer(0);
                            answer++;
                        }
                        else {
                            q.offer(w);
                            max += w;
                            answer++;
                            break;
                        }
                    }
                }
            }
            return answer + bridge_length;
        }
        
    }   

  ~~~
  3. 추가 설명
  ~~~
    총 4가지 경우를 고려한다
    1. Queue가 비어있음
    2. 트럭이 다리를 다 지남
    3. Queue가 비어있지 않음 & 다음 트럭을 넣으면 무게 초과 O
    4. Queue가 비어있지 않음 & 다음 트럭을 넣으면 무게 초과 X
    
    각각의 경우에서 대처방법은
    A1. Queue에 트럭의 무게를 넣는다
    A2. Queue의 크기와 다리 길이가 동일함을 의미. 이를 확인하고 Queue에서 꺼내 최대 무게에서 빼준다
    A3. Queue에 0을 넣는다
    A4. Queue에 트럭의 무게를 넣는다
  ~~~
</details>
