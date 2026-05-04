usage_tracker = {
    "claude-sonnet": {"calls": 0, "input_tokens": 0, "output_tokens": 0},
    "claude-haiku":  {"calls": 0, "input_tokens": 0, "output_tokens": 0},
}


def record_usage(model:str,input_tok:int,output_tok:int):
    tracker = usage_tracker[model] #get the inner dict
    tracker["calls"] +=1
    tracker["input_tokens"] += input_tok
    tracker["output_tokens"] += output_tok


record_usage("claude-sonnet",512,128)
record_usage("claude-sonnet",300,92)
record_usage("claude-haiku",200,60)


for model,status in usage_tracker.items():
    total = status["input_tokens"] +status["output_tokens"]
    print(f"{model}:{status['calls']} calls, {total} total tokens")


