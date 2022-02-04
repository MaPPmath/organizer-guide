correct = [1,0,1,0,0, 1,1,0,0,1, 0,0,0,1,1]

(0..14).to_a.each do |i|
  mod = correct.dup
  mod[i] = 1-correct[i]
  puts mod.map{|i|['I','P'][i]}.join("")+","
end
(0..14).to_a.permutation(2).each do |tuple|
  next if tuple[0]>tuple[1]
  mod = correct.dup
  mod[tuple[0]] = 1-correct[tuple[0]]
  mod[tuple[1]] = 1-correct[tuple[1]]
  puts mod.map{|i|['I','P'][i]}.join("")+","
end
