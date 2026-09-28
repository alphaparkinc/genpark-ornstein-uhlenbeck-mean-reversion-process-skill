"""MCP stdio server for Ornstein-Uhlenbeck Process."""
import sys
import json

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from client import OrnsteinUhlenbeckSimulator

def handle_rpc(request):
    req_id = request.get("id")
    method = request.get("method")
    params = request.get("params", {})

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "simulate_ornstein_uhlenbeck",
                        "description": "Simulate exact discrete path of mean-reverting OU process",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "x0": {"type": "number"},
                                "theta": {"type": "number", "description": "Speed of reversion"},
                                "mu": {"type": "number", "description": "Long-term mean"},
                                "sigma": {"type": "number", "description": "Volatility"},
                                "t_max": {"type": "number", "default": 1.0},
                                "steps": {"type": "integer", "default": 100},
                                "seed": {"type": "integer", "default": 42}
                            },
                            "required": ["x0", "theta", "mu", "sigma"]
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})
        if name == "simulate_ornstein_uhlenbeck":
            x0 = float(args.get("x0"))
            theta = float(args.get("theta"))
            mu = float(args.get("mu"))
            sigma = float(args.get("sigma"))
            t_max = float(args.get("t_max", 1.0))
            steps = int(args.get("steps", 100))
            seed = int(args.get("seed", 42))
            path = OrnsteinUhlenbeckSimulator.simulate_exact(x0, theta, mu, sigma, t_max, steps, seed)
            return {"jsonrpc": "2.0", "id": req_id, "result": {"path": path, "terminal_value": path[-1]}}
        return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": f"Method {name} not found"}}
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32600, "message": "Invalid request"}}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_rpc(req)
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()
        except Exception as e:
            sys.stdout.write(json.dumps({"jsonrpc": "2.0", "error": {"code": -32700, "message": str(e)}}) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
