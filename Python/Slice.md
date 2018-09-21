# Slice

slice는 start:stop[:step]의 형식으로 쓸 수있습니다. 여기서 [:step]은 써도 되고 안써도 된다는 의미입니다.

step을 명시하지 않을 경우에는

1. a[start:end] # start부터 end-1까지의 item
2. a[start:] # start부터 리스트 끝까지 item
3. a[:end] # 처음부터 end-1까지의 item
4. a[:] # 리스트의 모든 item
step value를 쓰는 경우에는

1. a[start:end:step]# start부터 end-1까지 step만큼 인덱스 증가시키면서
step을 지정할 때 :end에 유의하세요 end는 end부터 포함시키지 않겠다는 의미이지 end가 꼭 포함된다는 의미는 아닙니다.

또 start나 end가 음수가 음수인 경우에는 리스트의 끝에서부터 카운트하겠다는 의미입니다.

1. a[-1] # 맨 뒤의 item
2. a[-2:] # 맨 뒤에서부터 item2개
3. a[:-n] # 맨 뒤의 item n개 빼고 전부