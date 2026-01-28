JAVA_ANALYSIS_PROMPT = """
Return ONLY JSON.

{{
 "domain": string,
 "domain_summary": string,
 "endpoints":[{{"method":string,"path":string,"description":string}}],
 "entities":[{{"name":string,"fields":[string]}}],
 "enums":[string],
 "business_logic":[string],
 "usage_examples":[string]
}}

Controller:{controller}
Service:{service}
Models:{models}
"""
