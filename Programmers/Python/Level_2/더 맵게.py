import heapq

#heapq.heappush(heap, item) : item을 heap에 추가
#heapq.heappop(heap) : heap에서 가장 작은 원소를 pop & 리턴. 비어 있는 경우 IndexError가 호출됨. 
#heapq.heapify(x) : 리스트 x를 즉각적으로 heap으로 변환함 (in linear time, O(N) )
 
def solution(scoville, K):
    heapq.heapify(scoville)
    now = scoville[0]
    answer = 0 
    while now < K and len(scoville) > 1 :
            f = heapq.heappop(scoville)
            s = heapq.heappop(scoville)
            mix = f+s*2
            answer+=1
            heapq.heappush(scoville,mix)
            now = scoville[0]
    if min(scoville) < K:
        answer = -1
        
    return answer 
        
