# IT service continuity: a review checklist, not a recovery guarantee

A recovery objective on a spreadsheet can look reassuring. The harder questions are whether the service owner agrees with it, whether the dependencies are known, and whether anyone has exercised the recovery path recently.

I put together a small proof of concept to make those gaps easier to spot during a human review. It reads fictional service records and flags missing ownership, unconfirmed dependency maps, missing backup evidence, and recovery tests or planned test dates that appear overdue.

The tool does not decide whether an RTO or RPO is realistic. It cannot see a backup, inspect an application, or prove that a service can be restored. It simply surfaces what the sample record says, and what it does not say.

That distinction matters. A blank field is a prompt for the service owner, not a technical finding. A recorded backup indicator is an assertion, not proof. A test date is not evidence that a test succeeded.

The demo uses five fictional services and fixed rules. It has no infrastructure connection and runs no recovery action. Every result requires human review. Its value is as a conversation starter: which services have an accountable owner, what evidence supports the recovery assumptions, and when did the team last exercise the plan?

Project: https://github.com/shahidalparvezmalik/it-service-continuity-planner
Portfolio: https://shahidalparvezmalik.com/

About the author: Shahid Al Parvez Malik is a Senior IT Infrastructure & Service Delivery Manager with 20+ years of professional IT experience across infrastructure, IT Operations, ITSM, service delivery, systems administration, networking, technical support, procurement, and vendor management.

#IrishTech #IrishITTech #Ireland #ITOperations #ITInfrastructure #ServiceContinuity #DisasterRecovery
