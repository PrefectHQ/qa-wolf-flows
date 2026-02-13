from prefect import flow, task, get_run_logger
from prefect.events import emit_event
import logging

@task(log_prints=True)
def debug_task():
    """Task that logs at DEBUG level and emits an event"""
    logger = get_run_logger()
    logger.debug("Citizen monitoring system initialized. All movements will be recorded.")

    emit_event(
        event="citizen.surveillance.started",
        resource={"prefect.resource.id": "logging-system-debug"}
    )
    return "debug_complete"

@task(log_prints=True)
def info_task():
    """Task that logs at INFO level and emits an event"""
    logger = get_run_logger()
    logger.info("\033[36mDaily compliance check: 47,392 citizens scanned. 99.8% compliant.\033[0m")

    emit_event(
        event="citizen.compliance.checked",
        resource={"prefect.resource.id": "logging-system-info"}
    )
    return "info_complete"

@task(log_prints=True)
def warning_task():
    """Task that logs at WARNING level and emits an event"""
    logger = get_run_logger()
    logger.warning("Anomaly detected in sector 7G. Behavior pattern deviation: 2.3%")

    emit_event(
        event="citizen.anomaly.detected",
        resource={"prefect.resource.id": "logging-system-warning"}
    )
    return "warning_complete"

@task(log_prints=True)
def error_task():
    """Task that logs at ERROR level and emits an event"""
    logger = get_run_logger()
    logger.error("\033[31mUnauthorized thought pattern detected. Citizen #8473 flagged for re-education.\033[0m")

    emit_event(
        event="citizen.violation.logged",
        resource={"prefect.resource.id": "logging-system-error"}
    )
    return "error_complete"

@task(log_prints=True)
def critical_task():
    """Task that logs at CRITICAL level and emits an event"""
    logger = get_run_logger()
    logger.critical("CRITICAL: Mass non-compliance event. Initiating sector-wide memory adjustment protocol.")

    emit_event(
        event="system.critical.intervention",
        resource={"prefect.resource.id": "logging-system-critical"}
    )
    return "critical_complete"

@flow(log_prints=True)
def subflow_logger_flow():
    """Subflow that demonstrates all logging levels"""
    logger = get_run_logger()

    # Log at all levels in subflow body
    logger.debug("Subflow surveillance module active. Cross-referencing citizen databases...")
    logger.info("\033[32mSubflow compliance verification: All parameters within acceptable ranges.\033[0m")
    logger.warning("Subflow detected minor irregularity in logging patterns. Adjusting thresholds.")
    logger.error("Subflow error: One citizen attempted to access restricted memory sector.")
    logger.critical("\033[1m\033[33mSubflow critical alert: Central logging authority requires immediate status report.\033[0m")

    # Execute all logging tasks
    debug_task()
    info_task()
    warning_task()
    error_task()
    critical_task()

    return "subflow_complete"

@flow(log_prints=True)
def logger_flow():
    """Main flow that demonstrates comprehensive logging capabilities

## Flow purpose
This flow tests all Prefect logging levels and custom event emission.
Each task represents a different log level, and the flow emits multiple custom events.

## Flow code
```python
from prefect import flow, task, get_run_logger
from prefect.events import emit_event

@task(log_prints=True)
def debug_task():
    logger = get_run_logger()
    logger.debug("Debug level logging")
    emit_event(event="custom.debug.event", resource={"prefect.resource.id": "logger"})
    return "debug_complete"

# ... similar tasks for info, warning, error, critical ...

@flow(log_prints=True)
def logger_flow():
    logger = get_run_logger()

    # Log at all levels
    logger.debug("Flow debug message")
    logger.info("Flow info message")
    logger.warning("Flow warning message")
    logger.error("Flow error message")
    logger.critical("Flow critical message")

    # Emit custom events
    for i in range(5):
        emit_event(event=f"custom.flow.event.{i}", resource={"prefect.resource.id": "logger-flow"})

    # Execute tasks
    debug_task()
    info_task()
    warning_task()
    error_task()
    critical_task()

    # Call subflow
    subflow_logger_flow()
```
    """
    logger = get_run_logger()

    print("=== Central Logging Authority - Daily Operations Log ===")

    # Log at all levels in main flow body
    logger.debug("System initialization: Loading citizen behavior analysis algorithms...")
    logger.info("Morning report generated. All logging stations operational. Compliance rate: optimal.")
    logger.warning("\033[33mWarning: Detected 3 citizens reviewing historical records. Monitoring increased.\033[0m")
    logger.error("Error logged: Citizen attempted to modify personal log entries. Access denied.")
    logger.critical("\033[1m\033[31mCRITICAL ALERT: Someone is reading the logs. They know. Initiating protocol Omega-7.\033[0m")

    # Emit 5 custom events from main flow body
    emit_event(
        event="daily.log.cycle.started",
        resource={"prefect.resource.id": "central-logging-authority"}
    )

    emit_event(
        event="citizen.activity.aggregated",
        resource={"prefect.resource.id": "central-logging-authority"}
    )

    emit_event(
        event="compliance.metrics.calculated",
        resource={"prefect.resource.id": "central-logging-authority"}
    )

    emit_event(
        event="anomaly.patterns.analyzed",
        resource={"prefect.resource.id": "central-logging-authority"}
    )

    emit_event(
        event="memory.adjustment.scheduled",
        resource={"prefect.resource.id": "central-logging-authority"}
    )

    print("\033[34mExecuting logging diagnostics across all severity levels...\033[0m")

    # Execute all logging tasks
    debug_task()
    info_task()
    warning_task()
    error_task()
    critical_task()

    print("Initiating subflow analysis...")

    # Call the subflow
    subflow_logger_flow()

    logger.info("Daily logging cycle complete. All citizens remain compliant. Sleep well.")

    return "logging_complete"


if __name__ == '__main__':
    logger_flow.serve(name='dystopian-logger')
