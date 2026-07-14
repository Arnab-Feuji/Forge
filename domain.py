"""Domain logic for Medical Chatbot — driven by build_spec (BRD ACs + backlog + architecture)."""
from __future__ import annotations

import json
import os
import re
from typing import Any

BUILD_SPEC: dict[str, Any] = {
  "version": 1,
  "project_key": "MC",
  "project_name": "Medical Chatbot",
  "app_type": "Conversational AI Chatbot ",
  "app_kind": "chatbot",
  "summary": "Please develop a Medical Chatbot application based on 5 Agents like - Cancer Care, Diabetes, Mental Illness, Cardio & Respiratory\n\tConsider CDC & PubMed as RAG Database\n\tAdd features like chat message download button, Prescription download button, Mike button, Multimodal, Multilingual - Hindi, English & Spanish",
  "requirement_text": "Organisation: Feuji Software Solution Pvt. Ltd.\nSegment: Healthcare\n\nAI SUGGESTED & EDITED PARAMETERS:\nAPP TYPE: Conversational AI Chatbot\nSEGMENT: Healthcare\nPROBLEM: Develop a Medical Chatbot application featuring five specialty areas: Cancer Care, Diabetes, Mental Illness, Cardiology, and Respiratory Health. Utilize CDC and PubMed as primary Reference-as-a-Guide (RAG) databases. Incorporate features such as chat message and prescription downloads, voice input capability, and support for text, voice, and image modalities across multiple languages, including Hindi, English, and Spanish.\nTOOLS AND TECH STACKS: Python, FastAPI, React, PostgreSQL, TensorFlow\nKNOWLEDGE BASE SOURCES: CDC, PubMed, WHO guidelines, Clinical trials\nLLM FOUNDATION MODEL: GPT-4, BERT\nPERSONA AND TONE: Caring, knowledgeable, and patient-centric\nSUPPORTED LANGUAGES: English, Hindi, Spanish\nMULTIMODAL CAPABILITIES: Text, Voice, and Image understanding\nFALLBACK MECHANISMS: Escalate to human agent, Provide detailed error messages for user guidance\nEXPECTED OUTCOME: Deliver accurate and timely medical assistance, and streamline patient communications\nTARGET USER SPECIFICATION: Patients dealing with cancer, diabete",
  "requestor": "ad_isi03@hotmail.com",
  "deploy_port": 8095,
  "api": {
    "health": "/health",
    "meta": "/meta",
    "primary": "/chat",
    "stories": "/stories",
    "criteria": "/criteria"
  },
  "acceptance_criteria": [
    {
      "id": "AC-1",
      "given": "a valid request",
      "when": "rule BR-1 applies",
      "then": "Validate & sanitise all inputs against the declared schema."
    },
    {
      "id": "AC-2",
      "given": "a valid request",
      "when": "rule BR-2 applies",
      "then": "Log every decision/response immutably for audit."
    },
    {
      "id": "AC-3",
      "given": "a valid request",
      "when": "rule BR-3 applies",
      "then": "Produce cluster/anomaly assignments with a quality score."
    },
    {
      "id": "AC-4",
      "given": "a valid request",
      "when": "rule BR-4 applies",
      "then": "Persist the fitted model + assignment for each input row."
    }
  ],
  "business_rules": [
    {
      "id": "BR-1",
      "statement": "Validate & sanitise all inputs against the declared schema.",
      "rationale": ""
    },
    {
      "id": "BR-2",
      "statement": "Log every decision/response immutably for audit.",
      "rationale": ""
    },
    {
      "id": "BR-3",
      "statement": "Produce cluster/anomaly assignments with a quality score.",
      "rationale": ""
    },
    {
      "id": "BR-4",
      "statement": "Persist the fitted model + assignment for each input row.",
      "rationale": ""
    }
  ],
  "backlog": {
    "project": "MC",
    "total_points": 18,
    "epic_count": 3,
    "story_count": 3
  },
  "stories": [
    {
      "id": "S1",
      "title": "Implement BR-1..n as testable rules",
      "points": 8,
      "epic": "Rules Engine",
      "acceptance_criteria_ids": [],
      "acceptance_criteria": []
    },
    {
      "id": "S2",
      "title": "Decision + reasons response",
      "points": 5,
      "epic": "Rules Engine",
      "acceptance_criteria_ids": [],
      "acceptance_criteria": []
    },
    {
      "id": "S3",
      "title": "Decision API + audit log",
      "points": 5,
      "epic": "Service & Compliance",
      "acceptance_criteria_ids": [],
      "acceptance_criteria": []
    }
  ],
  "architecture": {
    "has_diagram": True,
    "modules": [
      "api",
      "domain",
      "ui",
      "data",
      "orchestration",
      "context"
    ],
    "services": [],
    "render_url": "https://mermaid.ink/img/pako:eNpVz70KgzAUBeBXuWRqodK_zaEgHULBYgkUh9ThNrliaKxwjZUivnurm8sZzneWMwjTWBKxKH3Tmwo5QKoeb4B7S7zSUxZriKITyFwntwtIDNTjt5g2Mp8lU2edsamoDYyh4dn-5YznnVYU2NGHGLagErnkvZYdsmV0vl3KQafpFUr0_onmtbSjTjrrQiE2oiau0VkRDyJUVE9fLJXY-SDG8Qdt6UWF",
    "excerpt": "%% C4 Context\nflowchart LR\n  User([User]) --> GW[API Gateway]\n  GW --> ORC[Orchestrator]\n  ORC --> C0[Retriever / RAG]\n  ORC --> C1[Guardrails]\n  ORC --> C2[LLM fallback]\n  ORC --> C3[Audit]\n\n%% Sequence\nsequenceDiagram\n  User->>ORC: message\n  ORC->>SAFE: guardrail check\n  ORC->>RAG: retrieve (sources)\n  RAG-->>ORC: passages + citation\n  ORC-->>User: answer + source\n\n%% ER\nerDiagram\n  MC_REQUEST ||--o| MC_RESPONSE : yields\n  MC_REQUEST ||--o{ AUDIT_EVENT : logs"
  },
  "modules": [
    "api",
    "domain",
    "ui",
    "data",
    "orchestration",
    "context"
  ],
  "input_fields": [
    {
      "name": "feature_a",
      "dtype": "float",
      "description": ""
    },
    {
      "name": "feature_b",
      "dtype": "float",
      "description": ""
    }
  ],
  "sample_input": {
    "feature_a": 42.5,
    "feature_b": 88.2
  },
  "output_fields": [],
  "rag_sources": [],
  "domains": [],
  "constraints": [],
  "nonfunctional": [],
  "escalation_phrases": [
    "can't breathe",
    "fraud"
  ],
  "model": {},
  "demo_scope": {
    "strategy": "sprint1_stories",
    "story_ids": [
      "S1",
      "S2",
      "S3"
    ],
    "ac_ids": [
      "AC-1",
      "AC-2",
      "AC-3",
      "AC-4"
    ],
    "rule_ids": [
      "BR-1",
      "BR-2",
      "BR-3",
      "BR-4"
    ]
  }
}

_SPEC_PATH = os.path.join(os.path.dirname(__file__), "build_spec.json")


def load_spec() -> dict[str, Any]:
    try:
        with open(_SPEC_PATH, encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return BUILD_SPEC


def meta() -> dict[str, Any]:
    s = load_spec()
    return {
        "project_key": s.get("project_key"),
        "project_name": s.get("project_name"),
        "app_type": s.get("app_type"),
        "app_kind": s.get("app_kind"),
        "summary": s.get("summary"),
        "primary_api": (s.get("api") or {}).get("primary"),
        "story_ids": [st.get("id") for st in (s.get("stories") or [])],
        "ac_ids": [a.get("id") for a in (s.get("acceptance_criteria") or [])],
        "rule_ids": [r.get("id") for r in (s.get("business_rules") or [])],
        "modules": s.get("modules") or [],
        "architecture_services": (s.get("architecture") or {}).get("services") or [],
        "demo_scope": s.get("demo_scope") or {},
        "backlog": s.get("backlog") or {},
    }


def list_stories() -> list[dict[str, Any]]:
    return list((load_spec().get("stories") or []))


def list_criteria() -> list[dict[str, Any]]:
    return list((load_spec().get("acceptance_criteria") or []))


def _norm_key(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", (name or "").strip().lower()).strip("_")


def _clean_payload(payload: dict[str, Any]) -> dict[str, Any]:
    return {_norm_key(k): v for k, v in (payload or {}).items()}


def evaluate_rules(payload: dict[str, Any]) -> dict[str, Any]:
    """Deterministic decision engine from BRD business rules."""
    s = load_spec()
    rules = s.get("business_rules") or []
    clean = _clean_payload(payload)
    reasons: list[str] = []
    checked: list[str] = []
    approved = True

    if not rules:
        return {
            "decision": "APPROVED",
            "reasons": ["No BRD business rules supplied — demo auto-approve."],
            "checked_rules": [],
            "echo": payload,
            "ac_ids": [a.get("id") for a in (s.get("acceptance_criteria") or [])],
        }

    for r in rules:
        rid = r.get("id") or "BR"
        stmt = str(r.get("statement") or "")
        checked.append(rid)
        stmt_clean = (stmt.replace("≤", "<=").replace("≥", ">=")
                          .replace("&le;", "<=").replace("&ge;", ">="))
        match = re.search(
            r"([a-zA-Z_][a-zA-Z0-9_\s-]*)\s*(>=|<=|==|!=|>|<|=)\s*([0-9.,]+)",
            stmt_clean,
        )
        if not match:
            # Soft text rule: fail closed if statement demands a requirement and no matching value present
            tokens = [w for w in re.findall(r"[a-zA-Z]{4,}", stmt_clean.lower()) if w not in {"must", "should", "shall", "only", "with", "from", "that", "this"}]
            hit = False
            for val in clean.values():
                if isinstance(val, str) and any(t in val.lower() for t in tokens[:4]):
                    hit = True
                    break
            if (not hit) and any(w in stmt_clean.lower() for w in ("must", "shall", "require", "only")):
                approved = False
                reasons.append(f"Failed {rid}: {stmt}")
            else:
                reasons.append(f"Noted {rid}: {stmt}")
            continue

        var_name = _norm_key(match.group(1))
        op = match.group(2).strip()
        if op == "=":
            op = "=="
        target = float(match.group(3).replace(",", ""))

        # FOIR special case often seen in lending BRDs
        if "foir" in var_name and "monthly_income" in clean:
            try:
                existing = float(clean.get("existing_emis", 0) or 0)
                new_emi = float(clean.get("new_emi", 0) or clean.get("emi", 0) or 0)
                income = float(clean["monthly_income"])
                actual = ((existing + new_emi) / income) * 100 if income else 999.0
            except Exception:
                approved = False
                reasons.append(f"Failed {rid}: cannot compute FOIR")
                continue
        elif var_name in clean:
            try:
                actual = float(clean[var_name])
            except Exception:
                approved = False
                reasons.append(f"Failed {rid}: field '{var_name}' is not numeric")
                continue
        else:
            approved = False
            reasons.append(f"Missing required field '{var_name}' for {rid}")
            continue

        passed = {
            ">=": actual >= target,
            "<=": actual <= target,
            ">": actual > target,
            "<": actual < target,
            "==": actual == target,
            "!=": actual != target,
        }.get(op, False)
        if not passed:
            approved = False
            reasons.append(f"Failed {rid}: {stmt} (actual {var_name}={actual})")
        else:
            reasons.append(f"Passed {rid}: {stmt}")

    return {
        "decision": "APPROVED" if approved else "DECLINED",
        "reasons": reasons,
        "checked_rules": checked,
        "echo": payload,
        "ac_ids": [a.get("id") for a in (s.get("acceptance_criteria") or [])],
        "story_ids": [st.get("id") for st in (s.get("stories") or [])],
    }


def build_knowledge() -> dict[str, str]:
    s = load_spec()
    kb: dict[str, str] = {
        "about": f"{s.get('project_name')} — {s.get('summary') or 'Forge lite demo'}",
        "project": str(s.get("project_key") or ""),
    }
    for src in (s.get("rag_sources") or []):
        kb[_norm_key(str(src))] = f"Knowledge source configured: {src}"
    for dom in (s.get("domains") or []):
        kb[_norm_key(str(dom))] = f"In-scope domain: {dom}"
    for r in (s.get("business_rules") or []):
        stmt = str(r.get("statement") or "")
        kb[_norm_key(r.get("id") or "rule")] = stmt
        for w in re.findall(r"[a-zA-Z]{5,}", stmt.lower())[:3]:
            kb.setdefault(w, stmt)
    for a in (s.get("acceptance_criteria") or []):
        then = str(a.get("then") or "")
        kb[_norm_key(a.get("id") or "ac")] = then
        for w in re.findall(r"[a-zA-Z]{5,}", then.lower())[:2]:
            kb.setdefault(w, then)
    for st in (s.get("stories") or []):
        title = str(st.get("title") or "")
        kb[_norm_key(st.get("id") or "story")] = f"Story {st.get('id')}: {title}"
        for w in re.findall(r"[a-zA-Z]{5,}", title.lower())[:2]:
            kb.setdefault(w, title)
    return kb


def chat_answer(message: str) -> dict[str, Any]:
    s = load_spec()
    text = (message or "").lower()
    escalations = [p.lower() for p in (s.get("escalation_phrases") or [])]
    if any(p and p in text for p in escalations):
        return {
            "answer": (
                f"Safety escalation for {s.get('project_name')}. "
                "This may require immediate human attention. Please use local emergency services if needed."
            ),
            "source": "SAFETY",
            "matched_ac": None,
            "story_ids": [st.get("id") for st in (s.get("stories") or [])],
        }

    kb = build_knowledge()
    for key, val in kb.items():
        if key and key in text:
            return {
                "answer": val,
                "source": "BUILD_SPEC_KB",
                "matched_key": key,
                "ac_ids": [a.get("id") for a in (s.get("acceptance_criteria") or [])],
                "story_ids": [st.get("id") for st in (s.get("stories") or [])],
            }

    # Topic fallback using domains / stories
    domains = s.get("domains") or []
    stories = s.get("stories") or []
    hint = domains[0] if domains else (stories[0].get("title") if stories else s.get("summary"))
    return {
        "answer": (
            f"{s.get('project_name')} assistant: {s.get('summary') or 'ready'}. "
            f"Ask about: {', '.join(st.get('id','')+': '+st.get('title','') for st in stories[:4]) or hint}."
        ),
        "source": "PROJECT_FALLBACK",
        "ac_ids": [a.get("id") for a in (s.get("acceptance_criteria") or [])],
        "story_ids": [st.get("id") for st in stories],
    }


def predict_payload(payload: dict[str, Any], model: Any = None) -> dict[str, Any]:
    s = load_spec()
    model_cfg = s.get("model") or {}
    feats = list(model_cfg.get("independent_variables") or [])
    target = model_cfg.get("dependent_variable")
    clean = _clean_payload(payload)
    if model is None:
        # Lightweight demo prediction from features so QA has project-specific output
        vals = [float(clean.get(_norm_key(f), clean.get(f, 0) or 0)) for f in feats] or [0.0]
        score = sum(vals) / max(len(vals), 1)
        return {
            "prediction": round(score, 4),
            "target": target,
            "features_used": feats,
            "mode": "heuristic_demo",
            "ac_ids": [a.get("id") for a in (s.get("acceptance_criteria") or [])],
            "story_ids": [st.get("id") for st in (s.get("stories") or [])],
        }
    import numpy as np
    x = np.array([[float(clean.get(_norm_key(f), clean.get(f, 0) or 0)) for f in feats]])
    try:
        if hasattr(model, "predict_proba"):
            proba = model.predict_proba(x)[0].tolist()
            pred = model.predict(x)[0]
            try:
                pred = pred.item()
            except Exception:
                pass
            return {"prediction": pred, "proba": proba, "target": target, "features_used": feats, "mode": "model"}
        pred = model.predict(x)[0]
        try:
            pred = pred.item()
        except Exception:
            pass
        return {"prediction": pred, "target": target, "features_used": feats, "mode": "model"}
    except Exception as e:
        return {"error": str(e), "features_used": feats}
