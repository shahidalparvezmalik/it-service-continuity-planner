# IT Service Continuity & Recovery Readiness: What a checklist can—and cannot—tell us

A recovery target may be written down. A backup may be marked as available. A test date may appear in a plan. Those entries help, but they do not prove that a service can be recovered when it matters.

For an IT operations leader, the useful next step is often a disciplined review: who owns the service, what does it depend on, what evidence supports the recovery assumptions, and when was the recovery path last exercised?

## Turning missing information into a review conversation

I built a small proof of concept to make some of those gaps visible. It reads five fictional service records and flags missing ownership, unconfirmed dependency maps, missing backup-evidence indicators, absent or old recovery-test dates, and overdue next-test dates.

The sample run assessed five services. Three had one or more review flags. The result is a checklist for a person to investigate, not a finding about a real service.

The records also carry Recovery Time Objectives (RTOs) and Recovery Point Objectives (RPOs). The program displays those supplied values; it does not decide whether they are suitable, agreed, or technically achievable.

## Evidence still needs a person

A blank owner field means the record needs attention. It does not identify who should own the service. A `backup_evidence=yes` entry is a fictional input value, not a verified backup. A recorded exercise date says nothing about whether the exercise succeeded or whether corrective actions were completed.

That distinction is important. A simple report can help structure the review, but it cannot replace service-owner confirmation, business impact analysis, technical evidence, or a properly authorized exercise.

## What this demo does not do

The project uses deterministic rules and synthetic data. It is not an AI model, a continuity plan, a recovery platform, or an assurance of recoverability. It has no infrastructure or backup integration, does not calculate business impact, does not validate RTO/RPO targets, and executes no failover or recovery actions. Every output requires human review.

For teams, the practical discussion is straightforward: which service records are incomplete, which dependencies need confirmation, and what evidence should be reviewed before the next exercise? The answers belong with the accountable owners and technical teams, not in an automated flag.

## A small, testable starting point

The repository includes a Python command-line demo, five fictional service records, unit tests, a data dictionary, and a suggested human review sequence. The tests and sample run verify the code's behavior on the bundled fixture only; they do not validate any organization's continuity arrangements.

Project: https://github.com/shahidalparvezmalik/it-service-continuity-planner  
Professional portfolio: https://shahidalparvezmalik.com/

## Further reading

The Business Continuity Institute's October 2026 session on critical third-party technology dependencies discusses mapping technology dependencies, hidden supplier risks, concentration, and single points of failure: https://www.thebci.org/resource/managing-critical-third-party-technology-dependencies.html

The Central Bank of Ireland describes DORA's ICT risk, resilience testing, incident management, and ICT third-party risk provisions for financial entities within its scope: https://www.centralbank.ie/regulation/digital-operational-resilience-act-dora

These sources provide professional context; this demo is not a DORA assessment or compliance tool.

## About the author

Shahid Al Parvez Malik is a Senior IT Infrastructure & Service Delivery Manager with 20+ years of professional IT experience across enterprise infrastructure, IT Operations, ITSM, service delivery, systems administration, networking, technical support, procurement, and vendor management.

#IrishTech #IrishITTech #Ireland #ITOperations #ITInfrastructure #ServiceContinuity #DisasterRecovery
